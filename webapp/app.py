import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/student_score_model.joblib")

# App title
st.title("🎓 Student Score Predictor")
st.write("Predict the student's Math Score based on academic details.")

# Input fields
reading_score = st.number_input(
    "Enter Reading Score",
    min_value=0,
    max_value=100,
    value=50
)

writing_score = st.number_input(
    "Enter Writing Score",
    min_value=0,
    max_value=100,
    value=50
)

gender = st.selectbox(
    "Select Gender",
    ["female", "male"]
)

race = st.selectbox(
    "Select Race/Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)

parent_edu = st.selectbox(
    "Parent Education",
    [
        "associate's degree",
        "bachelor's degree",
        "high school",
        "master's degree",
        "some college",
        "some high school"
    ]
)

lunch = st.selectbox(
    "Lunch Type",
    ["free/reduced", "standard"]
)

test_prep = st.selectbox(
    "Test Preparation",
    ["completed", "none"]
)

# Prediction button
if st.button("Predict Score"):

    input_data = pd.DataFrame({
        'reading score': [reading_score],
        'writing score': [writing_score],
        'gender_male': [1 if gender == "male" else 0],
        'race/ethnicity_group B': [1 if race == "group B" else 0],
        'race/ethnicity_group C': [1 if race == "group C" else 0],
        'race/ethnicity_group D': [1 if race == "group D" else 0],
        'race/ethnicity_group E': [1 if race == "group E" else 0],
        "parental level of education_bachelor's degree": [
            1 if parent_edu == "bachelor's degree" else 0
        ],
        'parental level of education_high school': [
            1 if parent_edu == "high school" else 0
        ],
        "parental level of education_master's degree": [
            1 if parent_edu == "master's degree" else 0
        ],
        'parental level of education_some college': [
            1 if parent_edu == "some college" else 0
        ],
        'parental level of education_some high school': [
            1 if parent_edu == "some high school" else 0
        ],
        'lunch_standard': [1 if lunch == "standard" else 0],
        'test preparation course_none': [
            1 if test_prep == "none" else 0
        ]
    })

    prediction = model.predict(input_data)

    score = prediction[0]

    st.success(f"📘 Predicted Math Score: {score:.2f}")

    if score >= 80:
        st.success("🌟 Excellent Performance")
    elif score >= 60:
        st.info("👍 Good Performance")
    elif score >= 40:
        st.warning("📚 Average Performance")
    else:
        st.error("⚠️ Needs Improvement")