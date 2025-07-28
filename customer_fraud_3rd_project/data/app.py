import streamlit as st
import joblib
import numpy as np

# Load the model and column names
model = joblib.load("data/model/fraud_detection_model.pkl")
X_train_columns = joblib.load("data/model/X_train_columns.pkl")


st.set_page_config(page_title="Fraud Detection App", layout="centered")

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details below to check for potential fraud.")

# Create input fields dynamically based on columns
input_data = []
for col in X_train_columns:
    value = st.number_input(f"{col}", step=0.1, format="%.4f")
    input_data.append(value)

if st.button("Check for Fraud"):
    # Convert to numpy array and reshape
    input_array = np.array(input_data).reshape(1, -1)

    # Predict
    prediction = model.predict(input_array)[0]
    proba = model.predict_proba(input_array)[0][1]

    if prediction == 1:
        st.error(f"🚨 Fraudulent Transaction Detected! (Risk: {proba:.2%})")
    else:
        st.success(f"✅ Transaction is Safe (Risk: {proba:.2%})")
