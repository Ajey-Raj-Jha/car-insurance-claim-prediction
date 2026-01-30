import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Car Insurance Claim Prediction",
    layout="wide"
)

# --------------------------------------------------
# Resolve base paths
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"

# --------------------------------------------------
# Load trained artifacts
# --------------------------------------------------
model = joblib.load(MODEL_DIR / "random_forest_model.pkl")
scaler = joblib.load(MODEL_DIR / "scaler.pkl")
feature_columns = joblib.load(MODEL_DIR / "feature_columns.pkl")

# 🔑 EXACT numerical features scaler was trained on
scaler_features = list(scaler.feature_names_in_)

# --------------------------------------------------
# UI: Title
# --------------------------------------------------
st.title("🚗 Car Insurance Claim Prediction")
st.caption("Predict the probability of an insurance claim using a trained ML model")
st.markdown("---")

# --------------------------------------------------
# UI: Numerical Inputs
# --------------------------------------------------
st.subheader("Policyholder & Vehicle Details")

col1, col2 = st.columns(2)

with col1:
    age_of_policyholder = st.slider("Age of Policyholder", 18, 80, 35)
    age_of_car = st.slider("Age of Car (years)", 0, 20, 5)
    ncap_rating = st.slider("NCAP Safety Rating", 0, 5, 3)
    airbags = st.number_input("Number of Airbags", min_value=0, max_value=10, value=2)

with col2:
    population_density = st.number_input("Population Density", min_value=0, value=1000)
    displacement = st.number_input("Engine Displacement (cc)", 500, 5000, 1200)
    gross_weight = st.number_input("Gross Vehicle Weight", 500, 5000, 1500)

st.markdown("---")

# --------------------------------------------------
# UI: Categorical Inputs
# --------------------------------------------------
st.subheader("Vehicle Configuration")

col3, col4 = st.columns(2)

with col3:
    segment = st.selectbox("Car Segment", ["A", "B1", "B2", "C1", "C2"])
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    transmission_type = st.selectbox("Transmission Type", ["Manual", "Automatic"])

with col4:
    area_cluster = st.selectbox("Area Cluster", [f"C{i}" for i in range(1, 22)])
    rear_brakes_type = st.selectbox("Rear Brakes Type", ["Drum", "Disc"])

st.markdown("---")

# --------------------------------------------------
# UI: Binary Inputs
# --------------------------------------------------
st.subheader("Safety & Assistance Features")

col5, col6 = st.columns(2)

with col5:
    is_esc = st.checkbox("Electronic Stability Control (ESC)")
    is_tpms = st.checkbox("Tyre Pressure Monitoring System (TPMS)")

with col6:
    is_brake_assist = st.checkbox("Brake Assist")
    is_parking_camera = st.checkbox("Parking Camera")

st.markdown("---")

# --------------------------------------------------
# Prediction Logic
# --------------------------------------------------
st.subheader("Prediction")

if st.button("Predict Claim Probability"):

    # ------------------------------
    # Raw input dictionary (schema-level)
    # ------------------------------
    input_data = {
        "age_of_policyholder": age_of_policyholder,
        "age_of_car": age_of_car,
        "population_density": population_density,
        "displacement": displacement,
        "gross_weight": gross_weight,
        "ncap_rating": ncap_rating,
        "airbags": airbags,
        "segment": segment,
        "fuel_type": fuel_type,
        "transmission_type": transmission_type,
        "area_cluster": area_cluster,
        "rear_brakes_type": rear_brakes_type,
        "is_esc": int(is_esc),
        "is_tpms": int(is_tpms),
        "is_brake_assist": int(is_brake_assist),
        "is_parking_camera": int(is_parking_camera),
    }

    # ------------------------------
    # Convert to DataFrame
    # ------------------------------
    input_df = pd.DataFrame([input_data])

    # ------------------------------
    # One-hot encode categoricals
    # ------------------------------
    input_df = pd.get_dummies(input_df)

    # ------------------------------
    # Align FULL training schema
    # ------------------------------
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    # ------------------------------
    # Scale ONLY features scaler was trained on
    # ------------------------------
    input_df[scaler_features] = scaler.transform(input_df[scaler_features])

    # ------------------------------
    # Predict
    # ------------------------------
    probability = model.predict_proba(input_df)[0][1]

    # ------------------------------
    # Display result
    # ------------------------------
    st.metric(
        label="Predicted Claim Probability",
        value=f"{probability:.2%}"
    )

    if probability >= 0.2:
        st.error("⚠️ High Risk Policyholder")
    elif probability >= 0.1:
        st.warning("🟡 Medium Risk Policyholder")
    else:
        st.success("✅ Low Risk Policyholder")
