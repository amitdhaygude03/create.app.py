import streamlit as st
import pickle
import pandas as pd

# Load model
with open("random_forest_classifier.pkl", "rb") as f:
    model = pickle.load(f)

# Define input form
st.title("🧠 Brain Tumor Type Predictor")

st.write("Enter patient details below to predict the tumor type:")

# User inputs
age = st.slider("Age", 1, 100, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
tumor_size = st.slider("Tumor Size (cm)", 0.1, 10.0, 2.5)
location = st.selectbox("Tumor Location", ["Frontal", "Parietal", "Temporal", "Occipital", "Cerebellum"])
histology = st.selectbox("Histology Type", ["Astrocytoma", "Glioblastoma", "Meningioma"])
stage = st.selectbox("Stage", ["I", "II", "III", "IV"])
symptom_1 = st.checkbox("Headache")
symptom_2 = st.checkbox("Nausea")
symptom_3 = st.checkbox("Vision Problems")
radiation = st.radio("Radiation Treatment", ["Yes", "No"])
surgery = st.radio("Surgery Performed", ["Yes", "No"])
chemo = st.radio("Chemotherapy", ["Yes", "No"])
survival_rate = st.slider("Expected Survival Rate (%)", 0, 100, 70)
growth_rate = st.slider("Tumor Growth Rate", 0.0, 5.0, 1.2)
family_history = st.radio("Family History", ["Yes", "No"])
mri_result = st.selectbox("MRI Result", ["Normal", "Abnormal"])
follow_up = st.radio("Follow-up Required", ["Yes", "No"])

# Encoding inputs (manual encoding)
gender_val = 1 if gender == "Male" else 0
location_val = {"Frontal": 0, "Parietal": 1, "Temporal": 2, "Occipital": 3, "Cerebellum": 4}[location]
histology_val = {"Astrocytoma": 0, "Glioblastoma": 1, "Meningioma": 2}[histology]
stage_val = {"I": 0, "II": 1, "III": 2, "IV": 3}[stage]
radiation_val = 1 if radiation == "Yes" else 0
surgery_val = 1 if surgery == "Yes" else 0
chemo_val = 1 if chemo == "Yes" else 0
family_val = 1 if family_history == "Yes" else 0
mri_val = 0 if mri_result == "Normal" else 1
follow_up_val = 1 if follow_up == "Yes" else 0

# Input DataFrame
input_data = pd.DataFrame([{
    "Age": age,
    "Gender": gender_val,
    "Tumor_Size": tumor_size,
    "Location": location_val,
    "Histology": histology_val,
    "Stage": stage_val,
    "Symptom_1": int(symptom_1),
    "Symptom_2": int(symptom_2),
    "Symptom_3": int(symptom_3),
    "Radiation_Treatment": radiation_val,
    "Surgery_Performed": surgery_val,
    "Chemotherapy": chemo_val,
    "Survival_Rate": survival_rate,
    "Tumor_Growth_Rate": growth_rate,
    "Family_History": family_val,
    "MRI_Result": mri_val,
    "Follow_Up_Required": follow_up_val
}])

# Prediction
if st.button("Predict Tumor Type"):
    prediction = model.predict(input_data)
    st.success(f"🧬 Predicted Tumor Type: {prediction[0]}")
