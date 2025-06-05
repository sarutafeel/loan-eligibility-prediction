# Loan Eligibility Prediction

This project uses a machine learning model to predict whether a loan application is likely to be approved based on applicant information. The model is trained on real-world data and deployed with a simple Streamlit web app for interactive use.

---

## Features

- Predict loan approval using user inputs
- Cleaned and preprocessed dataset
- Random Forest & XGBoost models tested
- Streamlit-powered web app interface
- Model saved and reused via `joblib`

---

## Model Performance

- **Accuracy**: ~78%
- **Precision / Recall**: High for loan approval (class 1)
- **Model used**: `RandomForestClassifier` and optionally `XGBClassifier`

---

## How to Use Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/sarutafeel/loan-eligibility-prediction.git
   cd loan-eligibility-prediction
2. python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. streamlit run app/streamlit_app.py
