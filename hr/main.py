import pandas as pd
import numpy as np
data = pd.read_csv("HRdata.csv")

data = data.drop(['EmployeeCount', 'StandardHours', 'Over18','Education','EnvironmentSatisfaction','RelationshipSatisfaction','YearsWithCurrManager'], axis=1)
print(data)

# Data Cleaning

print(data.isnull().sum())
print(data.isnull().values.any())

change_column_name = data.rename(columns={
    'Age': 'Employee_Age',
    'Attrition': 'Employee_Attrition',
    'BusinessTravel': 'Business_Travel',
    'NumCompaniesWorked': 'No_of_companies_worked',
    'TotalWorkingYears': 'Experence in Years',
    'TrainingTimesLastYear' : 'Training_month_last_year',
    'YearsAtCompany' : 'Experence_at_our_company',
    'YearsInCurrentRole' : 'Experence_in_current_role',
    'YearsSinceLastPromotion' : 'Last_promotion_years' 
    })

data = data.drop_duplicates()

data['Gender'] = data['Gender'].str.capitalize()

# Eliminate NaN values

data = data.dropna()

# Additional changes: Correct data types and handle outliers

data['EmployeeNumber'] = data['EmployeeNumber'].astype(int)
data = data[data['MonthlyIncome'] < data['MonthlyIncome'].quantile(0.99)]

# Optionally, save the cleaned data to a new CSV file

data.to_csv('Cleaned_HRdata.csv', index=False)

# Work with cleaned data set 
df = pd.read_csv("Cleaned_HRdata.csv")

# # ==================Explore data structure:=============

df.info()
print(df.shape)