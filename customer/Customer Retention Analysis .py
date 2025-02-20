import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("customer_retention.csv")

# Handle missing values
df.fillna(0, inplace=True)

# Convert dates to datetime format
df['Last_Purchase_Date'] = pd.to_datetime(df['Last_Purchase_Date'])

# Calculate Customer Lifetime Value (CLV)
df['CLV'] = df['Total_Spend'] / df['Subscription_Length']

# Plot Churn Distribution
sns.countplot(x=df['Churn'], palette="coolwarm")
plt.title("Customer Churn Distribution")
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Prepare data
X = df[['Subscription_Length', 'Total_Spend', 'CLV']]
y = df['Churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate Model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
