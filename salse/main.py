# ==================Import the dataset===============

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_excel("ECOMM DATA.xlsx")

# # ==================Explore data structure:=============

print(data.head(200))
data.info()
print(data.shape)

# # =================Check for missing values:==================

print(data.isnull().sum())
print(data.isnull().values.any())

# # =================Data cleaning:=====================

cleaned_data = (data.dropna(subset=["Postal Code"]))
print(cleaned_data.isnull().sem())
print(cleaned_data.shape)

# # ==================Summary statistics:=============

print(cleaned_data.describe())

# ==================data visualization=============

# HISTOGRAM

cleaned_data.hist(figsize=(12, 8))
plt.title("Histogram By Using All Data")
plt.show()

plt.hist(cleaned_data["Sales"], bins = 50)
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.title("Sales Distribution")
plt.show()
# # BOX 

cleaned_data.boxplot(figsize=(12, 8))
plt.show()
sns.boxplot(x = cleaned_data["Profit"] )
plt.title("Profit Destribution")
plt.show()

# PAIRPLOT

sns.pairplot(cleaned_data)
plt.title("Pairplot By Using All Data")
plt.show()

#  ======================Further Alalysis==================

# Most Sales product category
Most_Sales_category = cleaned_data.groupby('Category')['Sales'].sum()
print("\nMost Sales product category :\n" ,(Most_Sales_category))

# # most profitable product
Most_Profitable_Category = cleaned_data.groupby("Category")["Profit"].sum()
print("\nmost profitable product : \n" ,(Most_Profitable_Category))

#  profit per each Product
Most_Consumed_Country = cleaned_data.groupby("Product Name")["Profit"].sum()
print("\nprofit per each Product : \n" ,(Most_Consumed_Country))

# shiping cost by sub-category
Most_Shiping_Cost = cleaned_data.groupby("Sub-Category") ["Shipping Cost"].sum()
print("\nshiping cost by sub-category : \n" ,(Most_Shiping_Cost))