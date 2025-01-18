import os  # For environment variables and system-related operations
from flask import Flask, render_template, request, jsonify  # Flask framework for web application
import joblib  # For loading pre-trained models and preprocessing objects
import pandas as pd  # For data manipulation and conversion

from preprocessing.preprocessing import preprocessing  # Custom preprocessing function

# Load pre-trained machine learning model and preprocessing utilities
lgbm_model = joblib.load('models/lgbm_model.pkl')  # LightGBM model
one_hot_encoder = joblib.load('models/one_hot_encoder.pkl')  # OneHotEncoder for categorical features
min_max_scaler = joblib.load('models/min_max_scaler.pkl')  # MinMaxScaler for numeric feature scaling

# Initialize the Flask application
app = Flask(__name__)

# Define the expected input features
FEATURES = [
    "Gender", "Age", "Marital_Status", "Dependents", "Education",
    "Employment_Status", "Occupation_Type", "Residential_Status", "City/Town",
    "Annual_Income", "Monthly_Expenses", "Credit_Score", "Existing_Loans",
    "Total_Existing_Loan_Amount", "Outstanding_Debt", "Loan_History",
    "Loan_Amount_Requested", "Loan_Term", "Loan_Purpose", "Interest_Rate",
    "Loan_Type", "Co-Applicant", "Bank_Account_History",
    "Transaction_Frequency"
]

# Define the main route for the web application (renders a homepage)
@app.route('/', methods=['GET'])
def __main__():
    return render_template('index.html')  # Render the index.html page

# Define a route for prediction API
@app.route('/predict', methods=['POST'])
def predict():
    # Handle incoming data and make predictions

    # Determine content type and extract input data
    if request.content_type == 'application/json':
        input_data = request.json  # JSON data
    elif request.content_type == 'application/x-www-form-urlencoded':
        input_data = request.form.to_dict()  # Form data
    else:
        # Unsupported content type
        return jsonify({"error": "Unsupported Content-Type"}), 415

    # Check if all required features are present in the input
    missing_features = [f for f in FEATURES if f not in input_data]
    if missing_features:
        return jsonify({
            "error": f"Missing features in input: {missing_features}"
        }), 400  # Return error if features are missing

    # Convert input data into a DataFrame for preprocessing
    input_data = {feature: [input_data[feature]] for feature in FEATURES}  # Format input
    df = pd.DataFrame(input_data, columns=FEATURES)  # Create DataFrame

    # Preprocess the data
    scaled_data = preprocessing(df)  # Apply preprocessing steps

    # Make a prediction using the pre-trained model
    prediction = lgbm_model.predict(scaled_data)  # Predict loan approval status

    # Interpret the prediction result
    predict_result = "Approved" if int(prediction[0]) == 1 else "Rejected"

    # Return the prediction result as JSON
    return jsonify({'prediction': predict_result})

# Run the Flask application
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0', debug=True)  # Set up app to run on port 8080
