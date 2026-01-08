#load the pandas library
import pandas as pd

# Load the Netflix titles dataset
df = pd.read_csv('data/netflix_titles.csv')

# Basic Checks
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())