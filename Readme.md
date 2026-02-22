<div align="center">

# 🏦 Loan Approval Prediction System

!Python
!Flask
!Docker
!LightGBM
!Accuracy

**An end-to-end Machine Learning solution that automates loan eligibility assessments.**
<br>
From raw data analysis to a containerized web application.

</div>

---

## 📖 Project Overview

This project demonstrates a complete data science lifecycle applied to financial risk assessment. Starting with raw data from **Kaggle**, the workflow involves extensive statistical analysis, feature engineering, and model selection using **PyCaret**.

The final solution is a high-performance **LightGBM** model (achieving **88.9% accuracy**) deployed as a user-friendly Web UI and a robust REST API using **Flask** and **Docker**.

## 🚀 Key Features

### 🧠 Data Science & Machine Learning
- **Data Pipeline**: Comprehensive cleaning, statistical analysis, and feature engineering.
- **Model Selection**: Utilized **PyCaret** to compare multiple algorithms.
- **Best Model**: **LightGBM** was selected for its superior performance (88.9% Accuracy) and speed.
- **Optimization**: Fine-tuned hyperparameters to maximize precision and recall.

### 💻 Engineering & Deployment
- **Interactive Web UI**: A clean Bootstrap-based form for real-time predictions.
- **REST API**: Production-ready endpoint (`POST /predict`) supporting JSON and Form data.
- **Preprocessing Pipeline**: Automated encoding and scaling ensuring the model receives data in the exact format it was trained on.
- **Containerization**: Fully Dockerized for consistent deployment across any environment.

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| **Core** | Python 3.11 |
| **Machine Learning** | LightGBM, PyCaret, Scikit-Learn, Pandas, NumPy |
| **Web Framework** | Flask, Jinja2, Bootstrap 5 |
| **Deployment** | Docker, Gunicorn |

## Project Structure

```bash
Loan_Approval_End_To_End_Project/
├── app.py                      # Main Flask Application
├── Dockerfile                  # Docker configuration
├── requirements.txt            # Python dependencies
├── models/                     # Serialized ML artifacts
│   ├── lgbm_model.pkl          # Trained LightGBM Model
│   ├── one_hot_encoder.pkl     # Categorical Encoder
│   └── min_max_scaler.pkl      # Numerical Scaler
├── preprocessing/
│   └── preprocessing.py        # Custom transformation logic
├── templates/
│   └── index.html              # Web Interface
├── Data_Science_and_Analysis/  # EDA and Experimentation
│   ├── *.ipynb                 # Jupyter Notebooks (PyCaret, EDA)
│   └── *.csv                   # Datasets
└── img_result/                 # Screenshots/Results
```

## Required Input Features
All 24 fields must be provided:

1. `Gender`
2. `Age`
3. `Marital_Status`
4. `Dependents`
5. `Education`
6. `Employment_Status`
7. `Occupation_Type`
8. `Residential_Status`
9. `City/Town`
10. `Annual_Income`
11. `Monthly_Expenses`
12. `Credit_Score`
13. `Existing_Loans`
14. `Total_Existing_Loan_Amount`
15. `Outstanding_Debt`
16. `Loan_History`
17. `Loan_Amount_Requested`
18. `Loan_Term`
19. `Loan_Purpose`
20. `Interest_Rate`
21. `Loan_Type`
22. `Co-Applicant`
23. `Bank_Account_History`
24. `Transaction_Frequency`

## Output
The API returns:

```json
{
  "prediction": "Approved"
}
```

or

```json
{
  "prediction": "Rejected"
}
```

## Run Locally
### 1) Clone and enter the project directory
```bash
git clone <your-repo-url>
cd Loan_Approval_End_To_End_Project
```

### 2) Create a virtual environment and install dependencies
Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

macOS/Linux:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3) Start the app
```bash
python app.py
```

The service runs at `http://localhost:8080`.

## Run with Docker
### Build image
```bash
docker build -t loan-approval-app .
```

### Run container
```bash
docker run -p 8080:8080 loan-approval-app
```

Open `http://localhost:8080`.

## API Usage
Endpoint:
```text
POST /predict
```

Headers:
```text
Content-Type: application/json
```

Example `curl` request:
```bash
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Gender": "Female",
    "Age": 25,
    "Marital_Status": "Married",
    "Dependents": 2,
    "Education": "Graduate",
    "Employment_Status": "Employed",
    "Occupation_Type": "Business",
    "Residential_Status": "Own",
    "City/Town": "Urban",
    "Annual_Income": 139901,
    "Monthly_Expenses": 2533,
    "Credit_Score": 743,
    "Existing_Loans": 0,
    "Total_Existing_Loan_Amount": 10942,
    "Outstanding_Debt": 19822,
    "Loan_History": 0,
    "Loan_Amount_Requested": 24535,
    "Loan_Term": 209,
    "Loan_Purpose": "Home",
    "Interest_Rate": 4.27,
    "Loan_Type": "Secured",
    "Co-Applicant": "Yes",
    "Bank_Account_History": 8,
    "Transaction_Frequency": 20
  }'
```

## Notes
- If required fields are missing, the API returns `400` with the missing field list.
- If `Content-Type` is unsupported, the API returns `415`.
- `Data_Science_and_Analysis/` contains notebooks and datasets for EDA/model experimentation.

## License
No license is currently specified in this repository.
