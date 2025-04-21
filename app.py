import streamlit as st
import pandas as pd
import joblib

# Load model and expected columns
model = joblib.load("rf_diabetes_hospital_model.pkl")
expected_columns = joblib.load("feature_columns.pkl")

st.title("🏥 Readmission Risk Predictor")

# Hardcoded input options
age_options = ['[0-10]', '[10-20]', '[20-30]', '[30-40]', '[40-50]', '[50-60]', '[60-70]', '[70-80]', '[80-90]', '[90-100]']
gender_options = ['Male', 'Female']
race_options = ['Caucasian', 'AfricanAmerican', 'Hispanic', 'Asian', 'Other']
change_options = ['Ch', 'No']
med_options = ['Yes', 'No']

# Manual mappings based on training
age_map = {v: i for i, v in enumerate(age_options)}
gender_map = {'Male': 0, 'Female': 1}
race_map = {'Caucasian': 0, 'AfricanAmerican': 1, 'Hispanic': 2, 'Asian': 3, 'Other': 4}
change_map = {'Ch': 0, 'No': 1}
med_map = {'Yes': 1, 'No': 0}

# Input fields
age = st.selectbox("Age", age_options)
gender = st.radio("Gender", gender_options)
race = st.selectbox("Race", race_options)
time_in_hospital = st.slider("Days in hospital", 1, 14, 5)
num_lab_procedures = st.slider("Lab procedures", 0, 100, 40)
number_inpatient = st.slider("Inpatient visits (last year)", 0, 20, 0)
change = st.radio("Medication changed?", change_options)
diabetesMed = st.radio("On diabetes medication?", med_options)

if st.button("Predict"):
    input_dict = {
        'age': age_map[age],
        'gender': gender_map[gender],
        'race': race_map[race],
        'time_in_hospital': time_in_hospital,
        'num_lab_procedures': num_lab_procedures,
        'number_inpatient': number_inpatient,
        'change': change_map[change],
        'diabetesMed': med_map[diabetesMed]
    }

    input_df = pd.DataFrame([input_dict])
    input_df = input_df.reindex(columns=expected_columns, fill_value=0)

    pred = model.predict(input_df)[0]
    st.success("✅ Unlikely to be readmitted" if pred == 0 else "⚠️ Likely to be readmitted")
