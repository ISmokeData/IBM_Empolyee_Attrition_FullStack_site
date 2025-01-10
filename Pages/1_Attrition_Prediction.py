import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

st.header('IBM Attrition Prediction')
st.write("Please ensure that all information is filled out accurately and carefully to maintain professionalism and clarity.")
loaded_model = joblib.load('PickleFile\svc_model.pkl')


Business_Travel = st.selectbox('**Business Travel**', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
if Business_Travel == 'Travel_Rarely':
    Business_Travel = 0
elif Business_Travel == 'Travel_Frequently':
    Business_Travel = 1
else:
    Business_Travel = 3

daily_rate = st.number_input('**Daily Rate**', min_value=100, max_value=1500, value=100)

Department = st.selectbox('**Department**', ['Sales', 'Research & Development', 'Human Resources'])
if Department == 'Sales':
    Department = 2
elif Department == 'Research & Development':
    Department = 0
else:
    Department = 1

DistanceFromHome = st.number_input('**Distance From Home**', min_value=1, max_value=50, value=1)

education = st.selectbox('**Education**', ['Below College', 'College', 'Bachelor', 'Master', 'Doctor'])
if education == 'Below College':
    education = 1
elif education == 'College':
    education = 2
elif education == 'Bachelor':
    education = 3
elif education == 'Master':
    education = 4
else:
    education = 5

education_field = st.selectbox('**Education Field**', ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources','Other'])
if education_field == 'Life Sciences':
    education_field = 0
elif education_field == 'Medical':
    education_field = 2
elif education_field == 'Marketing':
    education_field = 5
elif education_field == 'Technical Degree':
    education_field = 3
elif education_field == 'Human Resources':
    education_field = 4
else:
    education_field = 1

gender = st.selectbox('**Gender**',['Male','Female'])
if gender == 'Male':
    gender = 0
else:
    gender = 1

job_role = st.selectbox('**Job Role**', ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director', 'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources'])
if job_role == 'Sales Executive':
    job_role = 0
elif job_role == 'Research Scientist':
    job_role = 1
elif job_role == 'Laboratory Technician':
    job_role = 2
elif job_role == 'Manufacturing Director':
    job_role = 3
elif job_role == 'Healthcare Representative':
    job_role = 4
elif job_role == 'Manager':
    job_role = 8
elif job_role == 'Sales Representative':
    job_role = 5
elif job_role == 'Research Director':
    job_role = 6
else:
    job_role = 7

marital_status = st.selectbox('**Marital Status**', ['Single', 'Married', 'Divorced'])
if marital_status == 'Single':
    marital_status = 0
elif marital_status == 'Married':
    marital_status = 1
else:
    marital_status = 2

job_satisfaction = st.selectbox('**Job Satisfaction**', ['Low', 'Medium', 'High', 'Very High'])
if job_satisfaction == 'Low':
    job_satisfaction = 1
elif job_satisfaction == 'Medium':
    job_satisfaction = 2
elif job_satisfaction == 'High':
    job_satisfaction = 3
else:
    job_satisfaction = 4

percentage_Salaryhike = st.number_input('**Percentage Salary Hike**', min_value=10, max_value=25, value=10)

performance_rating = st.selectbox('**Performance Rating**', ['Low', 'Good', 'Excellent', 'Outstanding'])
if performance_rating == 'Low':
    performance_rating = 1
elif performance_rating == 'Good':
    performance_rating = 2
elif performance_rating == 'Excellent':
    performance_rating = 3
else:
    performance_rating = 4

StockOptionLevel = st.number_input('**Stock Option Level**', min_value=0, max_value=3, value=0)

YearsSinceLastPromotion = st.number_input('**Years Since Last Promotion**', min_value=0, max_value=15, value=0)

pred_data = pd.DataFrame({'Business Travel': Business_Travel, 'Daily Rate': daily_rate, 'Department': Department, 'Distance From Home': DistanceFromHome, 'Education': education, 'Education Field': education_field,
              'gender':gender, 'Job Role': job_role, 'Job Satisfaction': job_satisfaction,'Marital Status': marital_status, 'Percentage Salary Hike': percentage_Salaryhike, 'Performance Rating': performance_rating,
                'Stock Option Level': StockOptionLevel, 'Years Since Last Promotion': YearsSinceLastPromotion}, index=[0])


ss = StandardScaler()
pred_data = ss.fit_transform(pred_data)


if st.button('Predict'):
    prediction = loaded_model.predict(pred_data)
    if prediction == 0:
        st.error('This employee is likely to stay.')
    else:
        st.success('This employee is likely to leave.')
