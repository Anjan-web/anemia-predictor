import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("anemia_model_no_15_19.pkl")

# These are the exact 14 features used during model training
feature_labels = {
    '103_Women_age_15_years_and_above_who_consume_alcohol_%': "Women (15+) who consume alcohol (%)",
    '13_Children_age_5_years_who_attended_pre-primary_school_during_the_school_year_2019-20_%': "Children (5 yrs) in pre-primary school (%)",
    '16_Women_age_20-24_years_married_before_age_18_years_%': "Women (20–24) married before age 18 (%)",
    '2_Population_below_age_15_years_%': "Population below age 15 (%)",
    '35_Mothers_who_consumed_iron_folic_acid_for_100_days_or_more_when_they_were_pregnant_%': "Mothers took IFA ≥100 days (%)",
    '36_Mothers_who_consumed_iron_folic_acid_for_180_days_or_more_when_they_were_pregnant_%': "Mothers took IFA ≥180 days (%)",
    '54_Children_age_12-23_months_who_have_received_the_first_dose_of_measles-containing_vaccine_MCV_%': "Children with MCV-1 (%)",
    '57_Children_age_12-23_months_who_have_received_3_doses_of_penta_or_hepatitis_B_vaccine_%': "Children with 3 doses HepB (%)",
    '69_Children_age_6-8_months_receiving_solid_or_semi-solid_food_and_breastmilk16_%': "Children 6–8m fed solid + breastmilk (%)",
    '76_Children_under_5_years_who_are_underweight_weight-for-age18_%': "Underweight children under 5 (%)",
    '78_Women_whose_Body_Mass_Index_BMI_is_below_normal_BMI_<185_kg/m221_%': "Women with low BMI (%)",
    '81_Children_age_6-59_months_who_are_anaemic_<110_g/dl22_%': "Children (6–59m) anaemic (%)",
    '82_Non-pregnant_women_age_15-49_years_who_are_anaemic_<120_g/dl22_%': "Non-pregnant women anaemic (%)",
    '83_Pregnant_women_age_15-49_years_who_are_anaemic_<110_g/dl22_%': "Pregnant women anaemic (%)"
}

st.title("Anemia Prevalence Prediction (Women 15–49 yrs)")
st.markdown("Provide district-level inputs below to estimate anemia prevalence:")

# Collect user inputs
user_input = {}
for key, label in feature_labels.items():
    user_input[key] = st.slider(label, 0.0, 100.0, 50.0)

input_df = pd.DataFrame([user_input])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted anemia prevalence: **{prediction:.2f}%**")
