import streamlit as st
import pandas as pd
import requests

st.title("Adult Income Prediction")

age = st.slider("Age", min_value=18, max_value=100, value=30)

workclass = st.selectbox("Workclass", [
                                            'Private',
                                            'Self-emp-inc',
                                            'Local-gov', 
                                            'State-gov',
                                            'Federal-gov', 
                                            'Self-emp-not-inc', 
                                            'Without-pay', 
                                            'Never-worked'
                                        ])

education = st.selectbox("Education", [
                                           '11th', 
                                           'HS-grad', 
                                           'Assoc-acdm', 
                                           'Some-college', 
                                           '10th',
                                           'Prof-school', 
                                           '7th-8th', 
                                           'Bachelors', 
                                           'Masters', 
                                           'Doctorate',
                                           '5th-6th', 
                                           'Assoc-voc', 
                                           '9th', 
                                           '12th', 
                                           '1st-4th', 
                                           'Preschool'
                                        ])

educational_num = st.number_input("Educational Num" , step = 1)

marital_status = st.selectbox("Marital Status", [
                                                    'Never-married', 
                                                    'Widowed', 
                                                    'Married-civ-spouse', 
                                                    'Divorced',
                                                    'Separated', 
                                                    'Married-spouse-absent', 
                                                    'Married-AF-spouse'
                                                ])

occupation = st.selectbox("Occupation", [
                                            'Craft-repair', 
                                            'Sales', 
                                            'Machine-op-inspct', 
                                            'Other-service',
                                            'Handlers-cleaners', 
                                            'Prof-specialty', 
                                            'Tech-support',
                                            'Adm-clerical', 
                                            'Protective-serv', 
                                            'Transport-moving',
                                            'Exec-managerial',
                                            'Farming-fishing', 
                                            'Priv-house-serv',
                                            'Armed-Forces'
                                            ])

relationship = st.selectbox("Relationship", [
                                                
                                                'Husband',
                                                'Wife',
                                                'Unmarried',
                                                'Own-child', 
                                                'Not-in-family', 
                                                'other-relative'

                                            ])

race = st.selectbox("Race", [
                                'White', 
                                'Black', 
                                'Amer-Indian-Eskimo',
                                'Asian-Pac-Islander',
                                'Other'
                            ])

gender = st.selectbox("Gender", [
                                    "Male",
                                    "Female"
                                ])

capital_gain = st.number_input("Capital Gain" , step = 1)

capital_loss = st.number_input("Capital Loss" , step = 1)

hours_per_week = st.slider("Hours Per Week", 1, 100, 40)


API_URL = "https://minhalali12-adult-income.hf.space/predict"

if st.button("Predict"):

    data = pd.DataFrame([{
        "age": int(age),
        "workclass": workclass,
        "education": education,
        "educational_num": int(educational_num),
        "marital_status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "gender": gender,
        "capital_gain": int(capital_gain),
        "capital_loss": int(capital_loss),
        "hours_per_week": int(hours_per_week)
    }])

    response = requests.post(API_URL, params=data)

    if response.status_code == 200:
        result = response.json()["prediction"]

        # convert 0/1 → label
        label = "<=50K" if result == 0 else ">50K"

        st.success(f"Prediction: {label}")
    else:
        st.error("API Error")
