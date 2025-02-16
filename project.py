import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# Corrected file path
data = pd.read_csv(r'C:\Users\vinay\Downloads\organizations-100.csv')

Display the first few rows of the DataFrame
print(data.head())

Display basic information about the DataFrame
print(data.info())

# Display summary statistics of the DataFrame
print(data.describe())

# Display the column names
print(data.columns)

# Example: Calculate the mean number of employees
mean_employees = data['Number of employees'].mean()
print(f'Mean number of employees: {mean_employees}')

# Example: Group data by industry and calculate the mean number of employees
grouped_data = data.groupby('Industry')['Number of employees'].mean()
print(grouped_data)



Example: Plot a histogram of the number of employees
plt.hist(data['Number of employees'], bins=20, edgecolor='k')
plt.xlabel('Number of Employees')
plt.ylabel('Frequency')
plt.title('Histogram of Number of Employees')
plt.show()

# Example: Plot a bar chart of the mean number of employees by industry
grouped_data.plot(kind='bar')
plt.xlabel('Industry')
plt.ylabel('Mean Number of Employees')
plt.title('Mean Number of Employees by Industry')
plt.show()

Save the cleaned data to a new CSV file
data.to_csv(r'C:\Users\vinay\Downloads\organizations-100.csv', index=False)