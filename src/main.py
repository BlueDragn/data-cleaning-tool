#load the pandas library
import pandas as pd
import matplotlib.pyplot as plt

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
'''Drop missing rows
df2 = df.dropna()
print("Original shape:", df.shape)
print("Shape after dropping rows with missing values:", df2.shape)
'''

for col in text_columns:
    df[col] = df[col].fillna("Unknown")
    print("\nColumn:", col)
    print(df[col].head(10))



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

print(df.isnull().any())
print(df.info())
print(df.describe())

# Explore key columns basic EDA(Distribution Analysis)
print("\nType:",df["type"].value_counts())
print("\nRelease Year:",df["release_year"].value_counts())
print("\nRating:",df["rating"].value_counts())
print("\nduration:",df["duration"].value_counts())
print("\nCountry:",df["country"].value_counts())

#Visualize the distributions
#1. Distribution of content types (Movie vs TV Show)
df['type'].value_counts().plot(kind='bar')
plt.title('Movie vs TV Show Distribution')
plt.xlabel('Content Type')
plt.ylabel('Count')

plt.savefig('output/type_distribution.png')
plt.clf()

#2. Distribution of release years
df['release_year'].value_counts().sort_index().plot()
plt.title('Netflix Content Release Trend')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')

plt.savefig('output/release_year_distribution.png')
plt.clf()

#3. Distribution by country
df["country"].value_counts().head(10).plot(kind='bar')
#4. Distribution of ratings
df['rating'].value_counts().plot(kind='bar')
#5. Distribution of durations (for movies and TV shows separately)
df['duration'].value_counts().head(10).plot(kind='bar')

