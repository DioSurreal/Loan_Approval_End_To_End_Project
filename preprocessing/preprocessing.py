from flask import jsonify  # For creating JSON responses (if needed)
import joblib  # For loading pre-trained models and preprocessing tools
import numpy as np  # For numerical computations
import pandas as pd  # For data manipulation

# Load the pre-trained preprocessing tools
one_hot_encoder = joblib.load('models/one_hot_encoder.pkl')  # OneHotEncoder for categorical data
min_max_scaler = joblib.load('models/min_max_scaler.pkl')  # MinMaxScaler for numerical data scaling

# Define the preprocessing function
def preprocessing(df):
    # Convert column names to lowercase for uniformity
    df.columns = df.columns.str.lower()
    
    # Create a new column to categorize transaction frequency into levels
    df['trans_freq_level'] = pd.cut(df['transaction_frequency'], bins=[5, 17, 23, float('inf')],
                                    labels=['Low', 'Meduium', 'High'])
    
    # Calculate the difference between monthly income and expenses
    df['diff_income_to_expenses'] = (df['annual_income'] / 12) - df['monthly_expenses']
    
    # Calculate the debt-to-income ratio
    df['debt_to_income_ratio'] = df['outstanding_debt'] / df['annual_income']
    
    # Calculate the loan-to-value ratio
    df['loan_to_value_ratio'] = df['loan_amount_requested'] / df['annual_income']
    
    # Calculate credit utilization
    df['credit_utilize'] = df['outstanding_debt'] / df['total_existing_loan_amount']

    # Select features that are relevant for the model
    selected_features = [
        'employment_status', 'credit_score','debt_to_income_ratio', 'income_to_expenses_ratio'
    ]
    df_selected = df[selected_features]  # Create a new DataFrame with selected features

    # Define categorical columns for encoding
    cat_cols = ['employment_status']

    # Perform one-hot encoding on categorical features
    df_encoded = pd.DataFrame(one_hot_encoder.transform(df_selected[cat_cols]))
    
    # Rename columns after encoding for clarity
    df_encoded.columns = one_hot_encoder.get_feature_names_out(cat_cols)

    # Drop original categorical columns and concatenate encoded ones
    df_selected = df_selected.drop(columns=cat_cols)  # Remove original categorical columns
    df_selected = pd.concat([df_selected, df_encoded], axis=1)  # Add encoded columns to the DataFrame

    # Define numeric columns to scale
    cols_to_scale = ['credit_score', 'debt_to_income_ratio', 'income_to_expenses_ratio']
    
    # Scale numerical columns using MinMaxScaler
    df_selected[cols_to_scale] = min_max_scaler.transform(df_selected[cols_to_scale])
    
    # Return the preprocessed DataFrame
    return df_selected
