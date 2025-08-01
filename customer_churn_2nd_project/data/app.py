import streamlit as st
import pandas as pd
import joblib
import os
print("Current working directory:", os.getcwd())


# Load the trained model and feature columns
model = joblib.load("data/gradient_boost_model.pkl")
# model = joblib.load("gradient_boost_model.pkl")

X_train_columns = joblib.load("data/X_train_columns.pkl").columns

st.set_page_config(page_title="Customer Churn Predictor", layout="wide")
st.title("🔍 Customer Churn Prediction App")

st.markdown("""
Enter customer information to predict whether the customer will churn or not.
""")

# Input form
with st.form("churn_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior_citizen = st.selectbox("Senior Citizen", [0, 1])
        partner = st.selectbox("Has Partner?", ["Yes", "No"])
        dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
        tenure = st.slider("Tenure (in months)", 0, 72, 12)

    with col2:
        monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
        total_charges = st.number_input("Total Charges", min_value=0.0, value=2000.0)
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

    submitted = st.form_submit_button("Predict")

    if submitted:
        # Create a DataFrame with user input
        user_input = pd.DataFrame([{
            "gender": gender,
            "SeniorCitizen": senior_citizen,
            "Partner": partner,
            "Dependents": dependents,
            "tenure": tenure,
            "MonthlyCharges": monthly_charges,
            "TotalCharges": total_charges,
            "Contract": contract,
            "PaymentMethod": payment_method,
            "InternetService": internet_service
        }])

        # One-hot encode to match training columns
        user_input_processed = pd.get_dummies(user_input)

        # Reindex to match training features
        user_input_processed = user_input_processed.reindex(columns=X_train_columns, fill_value=0)

        # Predict
        prediction = model.predict(user_input_processed)

        # Display result
        st.success("✅ The customer is likely to CHURN." if prediction[0] == 1 else "✅ The customer is NOT likely to churn.")
