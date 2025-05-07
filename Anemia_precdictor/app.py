import pandas as pd
import streamlit as st
import joblib
# Page config
st.set_page_config(page_title="Anemia Predictor", layout="wide")
st.title("🩸 Anemia Prevalence Predictor (15–49 years)")

# Load model
MODEL_PATH = "anemia_model_no_15_19.pkl"
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    st.error("Model not found. Make sure 'anemia_model_no_15_19.pkl' is in the folder.")
    st.stop()

# List of all features used in model
FEATURES = [
    'Female_population_age_6_years_and_above_who_ever_attended_school_%',
    'Women_age_15_years_and_above_who_use_any_kind_of_tobacco_%',
    'Men_age_15_years_and_above_who_use_any_kind_of_tobacco_%',
    'Women_age_15_years_and_above_who_consume_alcohol_%',
    'Men_age_15_years_and_above_who_consume_alcohol_%',
    'Children_age_5_years_who_attended_pre-primary_school_during_the_school_year_2019-20_%',
    'Women_who_are_literate4_%',
    'Women_with_10_or_more_years_of_schooling_%',
    'Women_age_20-24_years_married_before_age_18_years_%',
    'Women_age_15-19_years_who_were_already_mothers_or_pregnant_at_the_time_of_the_survey_%',
    'Women_age_15-24_years_who_use_hygienic_methods_of_protection_during_their_menstrual_period5_%',
    'Population_below_age_15_years_%',
    'Mothers_who_consumed_iron_folic_acid_for_100_days_or_more_when_they_were_pregnant_%',
    'Mothers_who_consumed_iron_folic_acid_for_180_days_or_more_when_they_were_pregnant_%',
    'Average_out-of-pocket_expenditure_per_delivery_in_a_public_health_facility_Rs',
    "Children_age_12-23_months_fully_vaccinated_based_on_information_from_either_vaccination_card_or_mother's_recall11_%",
    'Children_under_age_5_years_whose_birth_was_registered_with_the_civil_authority_%',
    'Children_age_12-23_months_fully_vaccinated_based_on_information_from_vaccination_card_only12_%',
    'Children_age_12-23_months_who_have_received_BCG_%',
    'Children_age_12-23_months_who_have_received_3_doses_of_polio_vaccine13_%',
    'Children_age_12-23_months_who_have_received_3_doses_of_penta_or_DPT_vaccine_%',
    'Children_age_12-23_months_who_have_received_the_first_dose_of_measles-containing_vaccine_MCV_%',
    'Children_age_24-35_months_who_have_received_a_second_dose_of_measles-containing_vaccine_MCV_%',
    'Children_age_12-23_months_who_have_received_3_doses_of_rotavirus_vaccine14_%',
    'Children_age_12-23_months_who_have_received_3_doses_of_penta_or_hepatitis_B_vaccine_%',
    'Children_age_9-35_months_who_received_a_vitamin_A_dose_in_the_last_6_months_%',
    'Children_age_12-23_months_who_received_most_of_their_vaccinations_in_a_public_health_facility_%',
    'Children_age_12-23_months_who_received_most_of_their_vaccinations_in_a_private_health_facility_%',
    'Children_under_age_3_years_breastfed_within_one_hour_of_birth15_%',
    'Children_under_age_6_months_exclusively_breastfed16_%',
    'Children_age_6-8_months_receiving_solid_or_semi-solid_food_and_breastmilk16_%',
    'Breastfeeding_children_age_6-23_months_receiving_an_adequate_diet16_17_%',
    'Non-breastfeeding_children_age_6-23_months_receiving_an_adequate_diet16_17_%',
    'Total_children_age_6-23_months_receiving_an_adequate_diet16_17_%',
    'Children_under_5_years_who_are_stunted_height-for-age18_%',
    'Children_under_5_years_who_are_underweight_weight-for-age18_%',
    'Women_whose_Body_Mass_Index_BMI_is_below_normal_BMI_<185_kg/m221_%',
    'Women_who_are_overweight_or_obese_BMI_≥250_kg/m221_%',
    'Women_who_have_high_risk_waist-to-hip_ratio_≥085_%',
    'Children_age_6-59_months_who_are_anaemic_<110_g/dl22_%',
    'Non-pregnant_women_age_15-49_years_who_are_anaemic_<120_g/dl22_%',
    'Pregnant_women_age_15-49_years_who_are_anaemic_<110_g/dl22_%'
]

# Sidebar input sliders for each feature
st.sidebar.header("📊 District-level NFHS-5 Inputs")
user_input = {}
for feat in FEATURES:
    user_input[feat] = st.sidebar.slider(
        label=feat.replace("_", " ").replace("%", "").strip(),
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

# Convert input to DataFrame
input_df = pd.DataFrame([user_input])

# Predict
if st.button("🔍 Predict Anemia Prevalence"):
    try:
        pred = model.predict(input_df)[0]
        st.success(f"Predicted Anemia Prevalence (Women 15–49 yrs): **{pred:.2f}%**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

# Footer
st.markdown("---")
st.caption("This tool uses a Random Forest model trained on NFHS-5 district-level indicators.")