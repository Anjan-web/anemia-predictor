import streamlit as st
import numpy as np
import joblib
import os
import streamlit as st
import os
st.title("🩺 Hypertension Risk Predictor (Improved)")
st.markdown("Fill in the health details below to check your risk of hypertension.")
try:
    model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    model = joblib.load(model_path)
except Exception as e:
    st.error("❌ Could not load the model. Make sure model.pkl is in the same folder as app.py.")
    st.stop()
hemoglobin = st.number_input("Hemoglobin Level (g/dL)", min_value=4.0, max_value=20.0, value=13.0)
age=st.number_input('Age', min_value=18,max_value=80)
sex=st.selectbox('Sex',['Femal','Male'])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0)
pregnancy = st.number_input("Pregnancy Count (0 if not applicable)", min_value=0, max_value=20)
smoking = st.selectbox("Do you smoke?", ["No", "Yes"])
physical_activity = st.selectbox("Physical Activity Level", ["Low", "Moderate", "High"])
salt_content = st.slider("Salt content in your diet (1 = low, 5 = high)", 1, 5, 3)
alcohol = st.number_input("Alcohol consumption (drinks per day)", min_value=0.0, max_value=10.0)
stress = st.slider("Stress Level (1 = none, 5 = very high)", 1, 5, 3)
genetic = st.slider("Genetic Pedigree Coefficient (0.0 - 2.0)", 0.0, 2.0, 0.5)
ckd = st.selectbox("Do you have chronic kidney disease?", ["No", "Yes"])
thyroid = st.selectbox("Do you have adrenal or thyroid disorders?", ["No", "Yes"])
sex = 1 if sex == "Male" else 0
smoking = 1 if smoking == "Yes" else 0
physical_activity = {"Low": 0, "Moderate": 1, "High": 2}[physical_activity]
ckd = 1 if ckd == "Yes" else 0
thyroid = 1 if thyroid == "Yes" else 0
input_data = np.array([[
    age, sex, bmi, pregnancy, smoking, physical_activity,
    salt_content, alcohol, stress, genetic, ckd, thyroid
]])
if st.button("Predict Hypertension Risk"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ You are at **high risk** for hypertension. Please consult a doctor.")
    else:
        st.success("✅ You appear to be at **low risk** for hypertension.")