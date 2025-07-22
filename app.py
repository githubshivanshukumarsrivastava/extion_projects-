import streamlit as st
import pandas as pd

# Title and description
st.title("🔧 Predictive Maintenance Dashboard")
st.markdown("""
This dashboard shows maintenance alerts based on Remaining Useful Life (RUL) predictions.
Adjust the threshold below to flag units needing attention.
""")

# Load data (you can also replace this with actual predictions or a CSV)
@st.cache_data
def load_alerts():
    # Replace with your actual alerts DataFrame or load from CSV
    alerts = pd.read_csv("alerts.csv")  # Make sure this file exists
    return alerts

alerts = load_alerts()

# Threshold slider
threshold = st.slider("Set RUL Threshold for Alerts:", min_value=1, max_value=50, value=20)

# Apply threshold
alerts['maintenance_alert'] = alerts['predicted_RUL'] < threshold
alerts_triggered = alerts[alerts['maintenance_alert'] == True]

# Display alerts
st.subheader("🔔 Maintenance Alerts")
st.write(f"Showing units with predicted RUL < {threshold}")
st.dataframe(alerts_triggered.sort_values(by='unit_number'))

# Optional: download CSV
st.download_button("📥 Download Alert Report", data=alerts_triggered.to_csv(index=False), file_name="maintenance_alerts.csv", mime="text/csv")


#  => & "C:\Users\SHIVANSHU SRIVASTAVA\AppData\Roaming\Python\Python311\Scripts\streamlit.exe" run app.py