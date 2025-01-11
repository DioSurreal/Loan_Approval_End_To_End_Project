import os
from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd

from preprocessing.preprocessing import preprocessing


# โหลดโมเดลและตัวช่วย
lgbm_model = joblib.load('models/lgbm_model.pkl')
one_hot_encoder = joblib.load('models/one_hot_encoder.pkl')
min_max_scaler = joblib.load('models/min_max_scaler.pkl')

app = Flask(__name__)

FEATURES = [
    "Gender", "Age", "Marital_Status", "Dependents", "Education",
    "Employment_Status", "Occupation_Type", "Residential_Status", "City/Town",
    "Annual_Income", "Monthly_Expenses", "Credit_Score", "Existing_Loans",
    "Total_Existing_Loan_Amount", "Outstanding_Debt", "Loan_History",
    "Loan_Amount_Requested", "Loan_Term", "Loan_Purpose", "Interest_Rate",
    "Loan_Type", "Co-Applicant", "Bank_Account_History",
    "Transaction_Frequency"
]


@app.route('/', methods=['GET'])
def __main__():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # try:
    # รับ JSON จาก client
    if request.content_type == 'application/json':
        input_data = request.json
    elif request.content_type == 'application/x-www-form-urlencoded':
        input_data = request.form.to_dict()
    else:
        return jsonify({"error": "Unsupported Content-Type"}), 415
    input_data = request.json
    # print(type(input_data))

    # ตรวจสอบว่ามีฟีเจอร์ครบหรือไม่
    missing_features = [f for f in FEATURES if f not in input_data]
    if missing_features:
        return jsonify({
            "error": f"Missing features in input: {missing_features}"
        }), 400

    # จัดเรียงข้อมูลตามลำดับฟีเจอร์

    input_data = {feature: [input_data[feature]] for feature in FEATURES}

    # แปลงข้อมูลเป็น DataFrame
    df = pd.DataFrame(input_data, columns=FEATURES)

    scaled_data = preprocessing(df)
    # ทำการพยากรณ์ด้วยโมเดล LGBM
    prediction = lgbm_model.predict(scaled_data)

    predict_result = "Approved" if int(prediction[0]) == 1 else "Rejected"

    return jsonify({'prediction': predict_result})

    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
