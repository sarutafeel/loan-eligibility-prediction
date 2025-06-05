import streamlit as st
import joblib
import numpy as np

# load trained model
model = joblib.load('models/loan_model.pkl')

st.title("Loan Eligibility Prediction App")

# input fields
gender = st.selectbox("Gender", ['Male', 'Female'])
married = st.selectbox("Married", ['Yes', 'No'])
education = st.selectbox("Education", ['Graduate', 'Not Graduate'])
self_employed = st.selectbox("Self Employed", ['Yes', 'No'])
applicant_income = st.number_input("Applicant Income")
coapplicant_income = st.number_input("Coapplicant Income")
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Term (in months)")
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ['Urban', 'Rural', 'Semiurban'])
dependents = st.selectbox("Number of Dependents", ['0', '1', '2', '3+'])
dep_1 = 1 if dependents == '1' else 0
dep_2 = 1 if dependents == '2' else 0
dep_3p = 1 if dependents == '3+' else 0

# manually encoded input
input_data = np.array([
    applicant_income, coapplicant_income, loan_amount, loan_term, credit_history,
    1 if gender == 'Male' else 0,
    1 if married == 'Yes' else 0,
    1 if education == 'Not Graduate' else 0,
    1 if self_employed == 'Yes' else 0,
    1 if property_area == 'Rural' else 0,
    1 if property_area == 'Semiurban' else 0,
    dep_1, dep_2, dep_3p
]).reshape(1, -1)

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success("Loan Approved" if prediction == 1 else "Loan Rejected")