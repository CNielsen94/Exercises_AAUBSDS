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
sc = StandardScaler()
# Database connection
print("Connecting to database...")
url = 'https://github.com/CNielsen94/Exercises_AAUBSDS/blob/main/MLOps_assignments/Assignment_three/Database/HR_DB.db?raw=true'
filename = 'HR_DB.db'
urllib.request.urlretrieve(url, filename)

with open('model.pkl','rb') as f:
    model = pickle.load(f)
    
age = st.text_input('Enter your age', value='')
income = st.slider('Select your monthly income', min_value=0, max_value=100000, step=100, value=5000)
education = st.selectbox('Select your education level', ['High School', 'College', 'Graduate School'])

# Create a button widget to make the prediction
if st.button('Predict'):
    # Convert user inputs into a list
    user_input = [age, income, education]
    user_input = sc.fit_transform(user_input)

    # Use the model to make predictions
    prediction = model.predict(user_input)

    # Display the prediction to the user
    if prediction == 0:
        st.success('You are not likely to churn.')
    else:
        st.success('You are likely to churn.')

conn = sqlite3.connect('HR_DB.db')
print("Connection established.")

# Setting up dataframe for EDA
print("Loading dataframes...")
query = 'SELECT * FROM EmployeeTiers'
employee_tiers = pd.read_sql(query, conn)

query = 'SELECT * FROM manager_survey'
manager_survey = pd.read_sql(query, conn)

query = 'SELECT * FROM employee_survey'
employee_survey = pd.read_sql(query, conn)

query = 'SELECT * FROM general'
df_general = pd.read_sql(query, conn)
print("Dataframes loaded.")

# Merging dataframe manager_survey to df_general based on 'EmployeeID'
print("Merging dataframes...")
df_general = df_general.merge(manager_survey[['EmployeeID', 'JobInvolvement', 'PerformanceRating', 'total_mn']], on='EmployeeID')
df_EDA = df_general.merge(manager_survey[['EmployeeID', 'JobInvolvement', 'PerformanceRating', 'total_mn']], on='EmployeeID')
# Merging dataframe employee_survey to df_general based on 'EmployeeID'
df_general = df_general.merge(employee_survey[['EmployeeID', 'EnvironmentSatisfaction', 'JobSatisfaction', 'WorkLifeBalance', 'total_em']], on='EmployeeID')
df_EDA = df_general.merge(manager_survey[['EmployeeID', 'JobInvolvement', 'PerformanceRating', 'total_mn']], on='EmployeeID')
print("Dataframes merged.")

# Dropping rows containing NaN-values
print("Dropping rows with NaN values...")
df_EDA.dropna(axis=0, inplace=True)
df_general.dropna(axis=0, inplace=True)
print("Rows dropped.")
mlflow.set_tracking_uri("sqlite:///HR_DB.db")
experiment_id = "1" 
run_id = "9e99a255ada3438badd5353d66b28e27"
# Get the metrics of your model 
metrics = mlflow.get_run(run_id).data.metrics
metrics_df = pd.DataFrame(metrics.items(), columns=["Metric", "Value"])
def app():
    st.set_page_config(page_title="Employee Attrition Analysis", page_icon=":guardsman:", layout="wide")

    st.title("Employee Attrition Analysis")

    st.sidebar.header("Select an analysis")

    analysis_type = st.sidebar.selectbox("", ["Exploratory Data Analysis (EDA)", "Predictive Modeling"])

    if analysis_type == "Exploratory Data Analysis (EDA)":
        st.subheader("Exploratory Data Analysis (EDA)")
        st.title("Machine Learning Model Metrics")
        st.write(metrics_df)
        url = 'https://raw.githubusercontent.com/CNielsen94/Exercises_AAUBSDS/main/MLOps_assignments/Assignment_three/Database/mlruns/1/9e99a255ada3438badd5353d66b28e27/artifacts/feature_importances.png'
        filename = 'feature_importances.png'
        urllib.request.urlretrieve(url, filename)
        img = Image.open("feature_importances.png")
        st.image(img, caption="Feature Importances Plot")
        # Age filter for talented employees
        print("Filtering by age...")
        df_EDA_u30 = df_EDA[df_EDA['Age'] < 30]

        # Filter for employees with higher manager survey score than employee survey score
        print("Filtering by survey score...")
        talented_employees = df_EDA_u30[(df_EDA_u30['total_mn_y'] - df_EDA_u30['total_em']) > 1]

        # Visualize attrition distribution
        print("Visualizing data...")
        fig, ax = plt.subplots()
        sns.countplot(data=df_general, x='Attrition', hue='Department')
        st.pyplot(fig)

if __name__ == '__main__':
    app()
