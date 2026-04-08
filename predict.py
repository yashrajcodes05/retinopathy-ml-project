"""
predict.py
----------
Standalone script to load the saved best retinopathy model
and make predictions on new patient data.

Usage:
    python predict.py
"""

import joblib
import numpy as np

# ── Load the saved model ──────────────────────────────────────────────────────
try:
    model = joblib.load("best_retinopathy_model.pkl")
    print("✅ Model loaded successfully.\n")
except FileNotFoundError:
    print("❌ Model file not found.")
    print("   Please run the notebook first to train and save the model.")
    exit(1)


# ── Prediction function ───────────────────────────────────────────────────────
def predict_retinopathy(age: float, sbp: float, dbp: float, cholesterol: float) -> str:
    """
    Predict whether a patient has diabetic retinopathy.

    Parameters
    ----------
    age         : Patient age (years)
    sbp         : Systolic blood pressure
    dbp         : Diastolic blood pressure
    cholesterol : Cholesterol level

    Returns
    -------
    str : "Retinopathy" or "No Retinopathy"
    """
    data = np.array([[age, sbp, dbp, cholesterol]])
    prediction = model.predict(data)[0]
    return "Retinopathy" if prediction == 1 else "No Retinopathy"


# ── Interactive demo ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Diabetic Retinopathy Prediction ===\n")

    try:
        age         = float(input("Enter Age           : "))
        sbp         = float(input("Enter SBP           : "))
        dbp         = float(input("Enter DBP           : "))
        cholesterol = float(input("Enter Cholesterol   : "))
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")
        exit(1)

    result = predict_retinopathy(age, sbp, dbp, cholesterol)

    print(f"\n🔮 Prediction: {result}")
    if result == "Retinopathy":
        print("⚠️  This patient may have Diabetic Retinopathy. Please consult a doctor.")
    else:
        print("✅ No signs of Diabetic Retinopathy detected.")
