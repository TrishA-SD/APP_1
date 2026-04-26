import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
model = pickle.load(open('lr_model.pkl', 'rb'))

# Title
st.title("Employee Attrition Prediction App 💼")
col1, col2 = st.columns(2)
with col1:
 age = st.number_input('Age', min_value=18, max_value=60,value=25)
 Department = st.selectbox('Department', ('Sales', 'Research & Development', 'Human Resources'))
 distance_from_home = st.number_input('Distance From Home', min_value=1, max_value=50, value=5)
 env_satisfaction = st.selectbox('Environment Satisfaction', (1, 2, 3, 4,5))
 MaritalStatus = st.selectbox('Marital Status', ('Single', 'Married', 'Divorced'))
 JobLevel = st.selectbox('Job Level', (1, 2, 3, 4, 5))
with col2:
 JobRole = st.selectbox('Job Role', ('Sales Executive', 'Research Scientist','Laboratory Technician', 'Manufacturing Director','Healthcare Representative', 'Manager','Sales Representative', 'Research Director','Human Resources'))
 monthly_income = st.number_input('Monthly Income',min_value=1000, max_value=20000, value=5000)
 years_at_company = st.number_input('Years at Company', min_value=0, max_value=40, value=2)
 overtime = st.selectbox('Overtime', ('Yes', 'No'))
 gender = st.selectbox('Gender', ('Male', 'Female'))
overtime = 1 if overtime == 'Yes' else 0
Gender_Female = 1 if gender == 'Female' else 0
Gender_Male = 1 if gender == 'Male' else 0
department_dict = { 'Sales': 2,'Research & Development': 1,'Human Resources': 0}
Department=department_dict[Department]
marital_dict = {'Single': 2,'Married': 1,'Divorced': 0}
MaritalStatus=marital_dict[MaritalStatus]
JobRole_dict={'Laboratory Technician':8,'Sales Executive':7,'Research Scientist':6,'Sales Representative':5,'Human Resources':4,'Manufacturing Director':3,'Healthcare Representative':2,'Manager':1,'Research Director':0}
JobRole= JobRole_dict[JobRole]
input_features = pd.DataFrame({
    'Age': [age],
    'Department': [Department],
    'DistanceFromHome': [distance_from_home],
    'EnvironmentSatisfaction': [env_satisfaction],
    'MaritalStatus': [MaritalStatus],
    'JobLevel': [JobLevel],
    'JobRole': [JobRole],
    'MonthlyIncome': [monthly_income],
    'YearsAtCompany': [years_at_company],
    'overtime': [overtime],
    'Gender_Female': [Gender_Female],
    'Gender_Male': [Gender_Male]
})
scaler = StandardScaler()
cols_to_scale = ['Age', 'DistanceFromHome', 'MonthlyIncome', 'YearsAtCompany']
input_features[cols_to_scale] =scaler.fit_transform(input_features[cols_to_scale])
if st.button('Predict'):
    prediction = model.predict(input_features)[0]

    if prediction == 1:
        st.error("⚠️ Employee likely to leave")
    else:
        st.success("✅ Employee likely to stay")