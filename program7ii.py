import pandas as pd
# Reading data from a CSV file
df = pd.read_csv('C:/Users/RVUW274/Desktop/admk')
# Display the first 6 rows
print("First 6 rows of the DataFrame:")
print(df.head(6))
# Displaying column names and data types
print("\nColumn names and data types:")
print(df.info())
