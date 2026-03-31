import pandas as pd

# Loading a CSV file into a DataFrame
df=pd.read_csv(r'C:/Users/RVUW274/Desktop/admk')

print("Original DataFrame:")
df

# Identifying missing values
print("\nMissing values in the DataFrame:")
print(df.isnull().sum())

# Filling missing values in the 'Age' column with the mean
df['Q1'].fillna(df['Q1'].mean(), inplace=True)

print("\nDataFrame after filling missing values in 'Q1' column:")
df
