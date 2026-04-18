import pandas as pd

df=pd.read_csv(r'C:\Users\USER\OneDrive - Tshwane University of Technology\Documents\GitHub\FUTURE_DS_01\Sample - Superstore.csv', encoding='latin-1')
print(df.head())
print(f"Success! Loaded {len(df)} rows")
print(df.shape) #How many rows and columns
print(df.columns.tolist()) #Column names
print(df.info()) #Basic info about each column
print(df.describe()) #Summar statistics for numeric columns

#What is the total sales and total profit?
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")

#Which product category has the highest sales?
category_sales= df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(category_sales)

#What is the average profit per order? 
avg_profit_per_row=df['Profit'].mean()
print(f"Average profit per transaction: ${avg_profit_per_row:,.2f}")

#Which region made the most profit?
region_profit=df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print(region_profit)

#How many orders were placed in each year?
df['Order Date']=pd.to_datetime(df['Order Date']) #Convert Order date to datetime format
df['Year']=df['Order Date'].dt.year #Extract year
orders_per_year=df.groupby('Year').size() #count orders per year
print(orders_per_year)

#Create a simple chart that shows which category drives revenue
import matplotlib.pyplot as plt

category_sales=df.groupby('Category')['Sales'].sum() #Group and sort

category_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product Category')
plt.ylabel('Sales (USD)')
plt.xlabel('Category')
plt.xticks(rotation=0)
plt.show()

