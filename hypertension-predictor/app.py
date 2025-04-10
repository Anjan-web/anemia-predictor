import streamlit as st
import numpy as np
import joblib
import os
import streamlit as st
import os

st.title("🩺 Hypertension Predictor - App Started ✅")

st.write("📁 Current directory:", os.getcwd())
st.write("📄 Files in this directory:", os.listdir())

model = joblib.load(os.path.join(os.path.dirname(__file__), "model.pkl"))
st.title("🩺 Hypertension Risk Predictor")
age = st.number_input("Age", min_value=1, max_value=120)
male = st.radio("Gender", ["Female", "Male"])
currentSmoker = st.radio("Do you currently smoke?", ["No", "Yes"])
cigsPerDay = st.slider("Cigarettes per day", 0, 50, 0)
BPMeds = st.radio("On BP medication?", ["No", "Yes"])
diabetes = st.radio("Diabetic?", ["No", "Yes"])
totChol = st.number_input("Total Cholesterol", min_value=100.0, max_value=600.0)
sysBP = st.number_input("Systolic BP", min_value=80.0, max_value=250.0)
diaBP = st.number_input("Diastolic BP", min_value=50.0, max_value=150.0)
BMI = st.number_input("BMI", min_value=10.0, max_value=60.0)
heartRate = st.number_input("Heart Rate", min_value=40.0, max_value=150.0)
glucose = st.number_input("Glucose", min_value=40.0, max_value=400.0)
male = 1 if male == "Male" else 0
currentSmoker = 1 if currentSmoker == "Yes" else 0
BPMeds = 1 if BPMeds == "Yes" else 0
diabetes = 1 if diabetes == "Yes" else 0
if st.button("Predict Hypertension Risk"):
    input_data = np.array([[male, age, currentSmoker, cigsPerDay, BPMeds, diabetes,
                            totChol, sysBP, diaBP, BMI, heartRate, glucose]])
    
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠️ High Risk of Hypertension!")
    else:
        st.success("✅ Low Risk of Hypertension")