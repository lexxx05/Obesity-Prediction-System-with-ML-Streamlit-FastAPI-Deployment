import streamlit as st
import json
import requests

# Judul Aplikasi
st.title("WeightWise")
st.markdown("### Your Personal Obesity Risk Forecaster")

# Input pengguna
st.write("")
st.write("Please fill in the following details:")

Gender = st.selectbox("Gender", ["Male", "Female"])
Age = st.slider("Age", 1, 100, 25)
Height = st.slider("Height (cm)", 100, 250, 170)
Weight = st.slider("Weight (kg)", 30, 200, 70)
family_history_with_overweight = st.selectbox("Family history of overweight?", ["Yes", "No"])
FAVC = st.selectbox("Do you consume high-calorie food?", ["Yes", "No"])
FCVC = st.slider("Frequency of consuming vegetables", 1.0, 3.0, 2.0)
NCP = st.slider("Meals per day", 1, 3, 2)
CAEC = st.selectbox("Snacking frequency", ["Never", "Sometimes", "Often", "Always"])
SMOKE = st.selectbox("Do you smoke?", ["Yes", "No"])
CH2O = st.slider("Water intake (liters/day)", 1.0, 3.0, 2.0)
SCC = st.selectbox("Do you control your calories?", ["Yes", "No"])
FAF = st.slider("Physical activity level", 1.0, 3.0, 2.0)
TUE = st.slider("Smartphone usage level", 1.0, 3.0, 2.0)
CALC = st.selectbox("Alcohol consumption frequency", ["Never", "Sometimes", "Often", "Always"])
MTRANS = st.selectbox("Main mode of transportation", ["Car", "Bicycle", "Motorcycle", "Public Transportation"])

# Kumpulkan input ke dalam dictionary
inputs = {
    "Gender": Gender,
    "Age": float(Age),
    "Height": Height,
    "Weight": Weight,
    "family_history_with_overweight": family_history_with_overweight,
    "FAVC": FAVC,
    "FCVC": FCVC,
    "NCP": float(NCP),
    "CAEC": CAEC,
    "SMOKE": SMOKE,
    "CH2O": CH2O,
    "SCC": SCC,
    "FAF": FAF,
    "TUE": TUE,
    "CALC": CALC,
    "MTRANS": MTRANS
}

headers = {"Content-Type": "application/json"}
url = "https://large-crabs-drive.loca.lt/predict"

# Tombol untuk memprediksi
if st.button("Predict"):
    res = requests.post(url=url, data=json.dumps(inputs), headers = headers)
    st.subheader(f"Result: You are {res.text}!")
