import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Over_All_Data_2024.csv')

# Convert 'Date/Time of Sale' to datetaime format
df['Date/Time of Sale'] = pd.to_datetime(df['Date/Time of Sale']) 

# **Descriptive Analysis**

# 1. Summary Statistics
print("\nDescriptive Statistics:\n", df.describe())

# 2. Product-wise Analysis
top_products = df['Product Name'].value_counts().head(10)
print("\nTop 10 Selling Products:\n", top_products)

product_sales = df.groupby('Product Name')['Sales Amount'].sum()
print("\nTotal Sales by Product:\n", product_sales)

# 3. Payment Method Analysis
payment_method_counts = df['Payment Method'].value_counts()
print("\nPayment Method Distribution:\n", payment_method_counts)

# **Diagnostic Analysis**

# 1. Daily Sales Trend
daily_sales = df.groupby('Date/Time of Sale')['Sales Amount'].sum()
plt.figure(figsize=(12, 6))
plt.plot(daily_sales)
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.title('Daily Sales Trend')
plt.show()

# 2. Monthly Sales Trend
monthly_sales = df.set_index('Date/Time of Sale').resample('M')['Sales Amount'].sum()
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales)
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Monthly Sales Trend')
plt.show()

# 3. Sales by Payment Method
sns.boxplot(x='Payment Method', y='Sales Amount', data=df)
plt.title('Sales Amount Distribution by Payment Method')
plt.show()

# 4. Product Sales Distribution
sns.histplot(df['Sales Amount'], bins=20)
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.title('Sales Amount Distribution')
plt.show()

# 5. Total Revenue
total_revenue = df['Sales Amount'].sum()
print("\nTotal Revenue:", total_revenue)

# 6. Visualizations
# 6.1 Bar Chart: Product Sales
plt.figure(figsize=(10, 5))
sns.barplot(x=product_sales.index, y=product_sales.values)
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.title('Total Sales by Product')
plt.xticks(rotation=45)
plt.show()

# 6.2 Bar Chart: Payment Method Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='Payment Method', data=df)
plt.xlabel('Payment Method')
plt.ylabel('Number of Transactions')
plt.title('Payment Method Distribution')
plt.show()