from flask import jsonify
import joblib
import numpy as np
import pandas as pd


one_hot_encoder = joblib.load('models/one_hot_encoder.pkl')
min_max_scaler = joblib.load('models/min_max_scaler.pkl')


def preprocessing(df):

        df.columns = df.columns.str.lower()
        df['age_group'] = pd.cut(df['age'], bins=[17, 24, 39, 55, float('inf')], labels=[
                                'Young Adult', 'Middle Adult', 'Middle Age', 'Early Retirement'])
        df['trans_freq_level'] = pd.cut(df['transaction_frequency'], bins=[
                                        5, 17, 23, float('inf')], labels=['Low', 'Meduium', 'High'])
        df['diff_income_to_expenses'] = (df['annual_income']/12) - df['monthly_expenses']
        df['debt_to_income_ratio'] = df['outstanding_debt'] / df['annual_income']
        df['loan_to_value_ratio'] = df['loan_amount_requested'] / df['annual_income']
        df['credit_utilize'] = df['outstanding_debt'] /df['total_existing_loan_amount']

        selected_features = ['age_group', 'employment_status', 'credit_score', 'loan_amount_requested', 'annual_income',
                            'debt_to_income_ratio', 'income_to_expenses_ratio', 'monthly_expenses']
        df_selected = df[selected_features]

        # Select categorical columns for encoding
        cat_cols = ['age_group', 'employment_status']

        df_encoded = pd.DataFrame(one_hot_encoder.transform(df_selected[cat_cols]))

        # Rename columns after encoding
        df_encoded.columns = one_hot_encoder.get_feature_names_out(cat_cols)

        # Drop original categorical columns and concatenate encoded ones
        df_selected = df_selected.drop(columns=cat_cols)
        df_selected = pd.concat([df_selected, df_encoded], axis=1)

        # Columns to scale (excluding loan_approval_status)
        cols_to_scale = ['credit_score', 'loan_amount_requested', 'annual_income',
                        'debt_to_income_ratio', 'income_to_expenses_ratio', 'monthly_expenses']
        df_selected[cols_to_scale] = min_max_scaler.transform(
            df_selected[cols_to_scale])
        return df_selected
