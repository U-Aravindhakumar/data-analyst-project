
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aravind@2004",
    database="sales_db",  # Make sure this is your actual database name
    use_pure=True
)


query = "SELECT * FROM customer_sales"
df = pd.read_sql(query, conn)
conn.close()

# print(df.head())
# print(df.isnull().sum())


plt.figure(figsize=(10,5))
sns.histplot(df['Purchase_Amount'],bins = 30,kde=True, color="blue")
plt.title("Distribution of Purchase Amount")
plt.show()


plt.figure(figsize=(10, 5))
sns.scatterplot(x=df['Annual_Income'], y=df['Spending_Score'], hue=df['Gender'])
plt.title("Customer Spending Score vs. Income")
plt.show()

# K-means clustering

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

features = df[['Annual_Income', 'Spending_Score']]
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
kmeans = KMeans(n_clusters=3, random_state=42)
df['Customer_Segment'] = kmeans.fit_predict(features_scaled)
plt.figure(figsize=(10, 5))
sns.scatterplot(x=df['Annual_Income'], y=df['Spending_Score'], hue=df['Customer_Segment'], palette="Set1")
plt.title("Customer Segmentation Based on Spending Score & Income")
plt.show()


#Time series analysis

from statsmodels.tsa.arima.model import ARIMA

df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'])
df.set_index('Purchase_Date', inplace=True)
sales_trend = df['Purchase_Amount'].resample('M').sum()
model = ARIMA(sales_trend, order=(5,1,0))
model_fit = model.fit()
forecast = model_fit.forecast(steps=6)
plt.figure(figsize=(12, 5))
plt.plot(sales_trend, label='Actual Sales')
plt.plot(forecast, label='Forecasted Sales', linestyle='dashed', color='red')
plt.legend()
plt.title("Sales Forecasting for Next 6 Months")
plt.show()



# # Close connections
# cursor.close()
# mydb.close()
