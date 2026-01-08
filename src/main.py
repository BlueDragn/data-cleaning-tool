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

#  Cleaning Step 1:  Handle missing values in text columns
text_columns = ['director', 'cast', 'country', 'date_added', 'rating', 'duration']
for col in text_columns:
    df[col] = df[col].fillna("Unknown")

print("\nMissing Values after cleaning text columns:")
print(df.isnull().sum())

# Cleaning Step 2: Check for duplicates and remove them
duplicate_count = df.duplicated().sum()
print("\nNumber of duplicate rows:", duplicate_count)
df = df.drop_duplicates()
print("Duplicate rows after removal:", df.duplicated().sum())
print("Shape after removing duplicates:", df.shape)

# Final Step: Save the cleaned dataset
df.to_csv("output/cleaned_data.csv", index=False)
print("\nCleaned data saved to 'output/cleaned_data.csv'")

# Basic Summary Statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))