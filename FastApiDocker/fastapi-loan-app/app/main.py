from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Load your model and scaler
model = joblib.load('loan_model_v2.pkl')
scaler = joblib.load('scaler.pkl')

app = FastAPI()

# Accept RAW features
class LoanRawFeatures(BaseModel):
    age: float
    Monthly_Income: float
    Loan_Tenure_Applied: float
    cibil_score: float
    Existing_EMI: float
    Loan_Amount_Applied: float

@app.post("/predict")
def predict_loan_status(features: LoanRawFeatures):
    # 1️⃣ Raw features
    age = features.age
    Monthly_Income = features.Monthly_Income
    Loan_Tenure_Applied = features.Loan_Tenure_Applied
    cibil_score = features.cibil_score
    Existing_EMI = features.Existing_EMI
    Loan_Amount_Applied = features.Loan_Amount_Applied

    # 2️⃣ Feature engineering exactly like training!
    Existing_EMI_log = np.log1p(Existing_EMI)
    Loan_Amount_Applied_log = np.log1p(Loan_Amount_Applied)
    EMI_to_Income_Ratio = Existing_EMI / Monthly_Income
    EMI_to_Income_Ratio_log = np.log1p(EMI_to_Income_Ratio)

    # 3️⃣ Create the final feature vector
    input_data = np.array([[
        age,
        Monthly_Income,
        Loan_Tenure_Applied,
        cibil_score,
        Existing_EMI_log,
        Loan_Amount_Applied_log,
        EMI_to_Income_Ratio_log
    ]])

    # 4️⃣ Scale using the saved scaler
    input_scaled = scaler.transform(input_data)

    # 5️⃣ Predict
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    return {
        "prediction": int(prediction),
        "probability": probability
    }
