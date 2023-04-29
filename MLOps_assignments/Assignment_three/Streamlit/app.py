import streamlit as st
import urllib.request
import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import mlflow
from PIL import Image
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import os

defaults = {'Age': 50,
            'BusinessTravel': 'Travel_Rarely', 
            'Department': 'Research & Development', 
            'Education': 3, 
            'EducationField': 'Life Sciences', 
            'Gender': 'Male',
            'JobLevel': 2,
            'JobRole': 'Sales Representative',
            'MaritalStatus': 'Married',
            'NumCompaniesWorked': 1,
            'PercentSalaryHike': 15,
            'StockOptionLevel': 0,
            'TrainingTimesLastYear': 3,
            'YearsSinceLastPromotion': 0,
            'YearsWithCurrManager': 0,
            'JobInvolvement': 2,
            'PerformanceRating': 3,
            'EnvironmentSatisfaction': 3,
            'JobSatisfaction': 3,
            'WorkLifeBalance': 3
           }


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Database connection
print("Connecting to database...")
url = 'https://github.com/CNielsen94/Exercises_AAUBSDS/blob/main/MLOps_assignments/Assignment_three/Database/HR_DB.db?raw=true'
filename = 'HR_DB.db'
urllib.request.urlretrieve(url, filename)

# Load the model from the pkl file
with open(os.path.join(BASE_DIR, 'model.pkl'), 'rb') as f:
    model = pickle.load(f)

# Define the columns to collect from the user
columns = ['Age', 'BusinessTravel', 'Department', 'Education', 'EducationField', 'Gender',
           'JobLevel', 'JobRole', 'MaritalStatus', 'NumCompaniesWorked',
           'PercentSalaryHike', 'StockOptionLevel', 'TrainingTimesLastYear',
           'YearsSinceLastPromotion', 'YearsWithCurrManager', 'JobInvolvement',
           'PerformanceRating', 'EnvironmentSatisfaction', 'JobSatisfaction',
           'WorkLifeBalance']

# Create a dictionary to store the user input
user_input = {}

# Collect the user input using Streamlit widgets
for col in columns:
    user_input[col] = st.text_input(col)

# Convert the user input into a DataFrame
input_df = pd.DataFrame(user_input, index=[0])
input_df = input_df.fillna(defaults)

#Create list of object data types in df
others = input_df.select_dtypes('object').columns

# Perform label encoding
label_encoder = LabelEncoder()
for col in others:
    input_df[col] = label_encoder.fit_transform(input_df[col])

# Perform standard scaling
scaler = StandardScaler()
input_df = scaler.fit_transform(input_df)

# Make predictions using the model
prediction = model.predict(input_df)

# Display the prediction to the user
if prediction == 0:
    st.success('You are not likely to churn.')
else:
    st.success('You are likely to churn.')

if __name__ == '__main__':
    app()
