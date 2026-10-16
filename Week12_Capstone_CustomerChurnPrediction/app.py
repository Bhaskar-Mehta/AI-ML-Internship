import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Customer Churn Predictor", page_icon="📉")


@st.cache_resource
def load_bundle():
    return joblib.load("churn_model.joblib")


bundle = load_bundle()
model = bundle["model"]
options = bundle["options"]

st.title("Customer Churn Predictor")
st.write("Enter a telecom customer's details to estimate the chance they will leave. "
         "Trained on the Telco Customer Churn dataset (7,043 customers).")

col1, col2 = st.columns(2)

with col1:
    tenure = st.slider("Tenure (months with the company)", 0, 72, 12)
    monthly = st.number_input("Monthly charges ($)", 15.0, 130.0, 70.0, step=1.0)
    contract = st.selectbox("Contract", options["Contract"])
    internet = st.selectbox("Internet service", options["InternetService"])
    payment = st.selectbox("Payment method", options["PaymentMethod"])
    paperless = st.selectbox("Paperless billing", options["PaperlessBilling"])
    gender = st.selectbox("Gender", options["gender"])
    senior = st.selectbox("Senior citizen", options["SeniorCitizen"],
                          format_func=lambda v: "Yes" if v == 1 else "No")

with col2:
    partner = st.selectbox("Has partner", options["Partner"])
    dependents = st.selectbox("Has dependents", options["Dependents"])
    phone = st.selectbox("Phone service", options["PhoneService"])
    multiple = st.selectbox("Multiple lines", options["MultipleLines"])
    security = st.selectbox("Online security", options["OnlineSecurity"])
    backup = st.selectbox("Online backup", options["OnlineBackup"])
    protection = st.selectbox("Device protection", options["DeviceProtection"])
    support = st.selectbox("Tech support", options["TechSupport"])
    tv = st.selectbox("Streaming TV", options["StreamingTV"])
    movies = st.selectbox("Streaming movies", options["StreamingMovies"])

if st.button("Predict churn risk"):
    row = {
        "gender": gender, "SeniorCitizen": senior, "Partner": partner, "Dependents": dependents,
        "tenure": tenure, "PhoneService": phone, "MultipleLines": multiple,
        "InternetService": internet, "OnlineSecurity": security, "OnlineBackup": backup,
        "DeviceProtection": protection, "TechSupport": support, "StreamingTV": tv,
        "StreamingMovies": movies, "Contract": contract, "PaperlessBilling": paperless,
        "PaymentMethod": payment, "MonthlyCharges": monthly,
        "TotalCharges": tenure * monthly,   # estimated from tenure x monthly charges
    }
    data = pd.DataFrame([row])[bundle["columns"]]
    prob = float(model.predict_proba(data)[0, 1])

    if prob >= 0.6:
        st.error(f"High churn risk: {prob*100:.1f}%")
    elif prob >= 0.4:
        st.warning(f"Medium churn risk: {prob*100:.1f}%")
    else:
        st.success(f"Low churn risk: {prob*100:.1f}%")
    st.progress(prob)
    st.caption("TotalCharges is estimated as tenure x monthly charges. "
               "The model is a screening tool, not a guarantee.")