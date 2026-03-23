import streamlit as st
import numpy as np
import joblib

# --- Page Config ---
st.set_page_config(
    page_title="Insurance Charge Predictor",
    page_icon="🏥",
    layout="centered"
)

# --- Load Model & Scaler ---
@st.cache_resource
def load_artifacts():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

model, scaler = load_artifacts()

# --- UI ---
st.title("🏥 Insurance Charge Predictor")
st.markdown("Estimate your medical insurance charges based on your profile.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
    children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
    sex = st.selectbox("Sex", ["Male", "Female"])

with col2:
    smoker = st.selectbox("Smoker?", ["No", "Yes"])
    region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

st.divider()

# --- Feature Engineering ---
def prepare_input(age, bmi, children, sex, smoker, region):
    is_female = 1 if sex == "Female" else 0
    is_smoker = 1 if smoker == "Yes" else 0
    region_northwest = 1 if region == "Northwest" else 0
    region_southeast = 1 if region == "Southeast" else 0

    # BMI category (Obese = BMI > 29.9)
    bmi_category_obese = 1 if bmi > 29.9 else 0

    # Scale age, bmi, children
    scaled = scaler.transform([[age, bmi, children]])
    age_s, bmi_s, children_s = scaled[0]

    features = np.array([[
        age_s, is_female, bmi_s, children_s,
        is_smoker, region_southeast, bmi_category_obese, region_northwest
    ]])
    return features

if st.button("💰 Predict My Charges", use_container_width=True):
    features = prepare_input(age, bmi, children, sex, smoker, region)
    prediction = model.predict(features)[0]
    prediction = max(prediction, 0)  # no negative charges

    st.success(f"### Estimated Annual Charge: **${prediction:,.2f}**")

    # Insight callouts
    st.markdown("#### Key Factors:")
    if smoker == "Yes":
        st.warning("🚬 Smoking significantly increases your insurance charges.")
    if bmi > 29.9:
        st.warning("⚖️ Obesity (BMI > 30) is associated with higher charges.")
    if smoker == "No" and bmi <= 29.9:
        st.info("✅ Great profile! Non-smokers with healthy BMI typically pay less.")

st.divider()
st.caption("Model: Linear Regression | Dataset: Insurance CSV | Built with Streamlit")
