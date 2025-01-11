<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loan Application</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>
    <div class="container mt-5">
        <h1 class="text-center mb-4">Loan Application Form</h1>
        <form action="/predict" method="POST">
            <div class="row">
                <div class="col-md-6 mb-3">
                    <label for="gender" class="form-label">Gender:</label>
                    <select name="Gender" id="gender" class="form-select">
                        <option value="Female">Female</option>
                        <option value="Male">Male</option>
                    </select>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="age" class="form-label">Age:</label>
                    <input type="number" name="Age" id="age" class="form-control" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 mb-3">
                    <label for="marital_status" class="form-label">Marital Status:</label>
                    <select name="Marital_Status" id="marital_status" class="form-select">
                        <option value="Married">Married</option>
                        <option value="Single">Single</option>
                        <option value="Divorced">Divorced</option>
                    </select>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="dependents" class="form-label">Dependents:</label>
                    <input type="number" name="Dependents" id="dependents" class="form-control" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 mb-3">
                    <label for="education" class="form-label">Education:</label>
                    <select name="Education" id="education" class="form-select">
                        <option value="Graduate">Graduate</option>
                        <option value="High School">High School</option>
                        <option value="Postgraduate">Postgraduate</option>
                    </select>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="employment_status" class="form-label">Employment Status:</label>
                    <select name="Employment_Status" id="employment_status" class="form-select">
                        <option value="Employed">Employed</option>
                        <option value="Self-Employed">Self-Employed</option>
                        <option value="Unemployed">Unemployed</option>
                    </select>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 mb-3">
                    <label for="occupation_type" class="form-label">Occupation Type:</label>
                    <select name="Occupation_Type" id="occupation_type" class="form-select">
                        <option value="Salaried">Salaried</option>
                        <option value="Business">Business</option>
                        <option value="Others">Others</option>
                    </select>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="residential_status" class="form-label">Residential Status:</label>
                    <select name="Residential_Status" id="residential_status" class="form-select">
                        <option value="Owned">Owned</option>
                        <option value="Rented">Rented</option>
                        <option value="Mortgage">Mortgage</option>
                    </select>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 mb-3">
                    <label for="city" class="form-label">City/Town:</label>
                    <input type="text" name="City/Town" id="city" class="form-control" required>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="annual_income" class="form-label">Annual Income:</label>
                    <input type="number" name="Annual_Income" id="annual_income" class="form-control" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 mb-3">
                    <label for="monthly_expenses" class="form-label">Monthly Expenses:</label>
                    <input type="number" name="Monthly_Expenses" id="monthly_expenses" class="form-control" required>
                </div>
                <div class="col-md-6 mb-3">
                    <label for="credit_score" class="form-label">Credit Score:</label>
                    <input type="number" name="Credit_Score" id="credit_score" class="form-control" required>
                </div>
            </div>
            <label>Existing Loans:</label>
        <input type="number" name="Existing_Loans" required><br>
        <label>Total Existing Loan Amount:</label>
        <input type="number" name="Total_Existing_Loan_Amount" required><br>
        <label>Outstanding Debt:</label>
        <input type="number" name="Outstanding_Debt" required><br>
        <label>Loan_History:</label>
        <input type="number" name="Loan_History" required><br>
        <!-- Add fields for all other features similarly -->
        <label>Loan Amount Requested:</label>
        <input type="number" name="Loan_Amount_Requested" required><br>
        <label>Loan Term:</label>
        <input type="number" name="Loan_Term" required><br>
        <label>LoanPurposeLoan:</label>
        <input type="text" name="Loan_Purpose" required><br>
        <label>Loan Purpose:</label>
        <input type="text" name="Loan_Purpose" required><br>
        <label>Interest Rate:</label>
        <input type="number" name="Interest_Rate" required><br>
        <label>Loan Type:</label>
        <select name="Loan_Purpose">
            <option value="Secured">Secured</option>
            <option value="Unsecured">Unsecured</option>
        </select><br>
        <label>Co-Applicant:</label>
        <select name="Co-Applicant">
            <option value="Yes">Yes</option>
            <option value="No">No</option>
        </select><br>
        
        <label>Bank Account History:</label>
        <input type="number" name="Bank_Account_History" required><br>
        <label>Transaction Frequency:</label>
        <input type="number" name="Transaction_Frequency" required><br>
        <label>Default Risk:</label>
        <input type="number" name="Default_Risk" required><br>

            <!-- Repeat similar structure for other fields -->
            <div class="row">
                <div class="col-md-12 text-center">
                    <button type="submit" class="btn btn-primary w-50">Submit Application</button>
                </div>
            </div>
        </form>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>
