# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


print("my first python/script/recipe")
#"C:\Users\cash\OneDrive\Documents\css2024_day1"

import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset

df = pd.read_csv(r"C:\Users\cash\OneDrive\Documents\css2024_day1\movie_dataset.csv")


print(df.head())
print(df.info())
df.plot()

print(df.isnull().sum())


df.fillna(df.mean(), inplace=True)


df.dropna(subset=['categorical_column'], inplace=True)

# Rename columns without spaces for convenience
df.columns = df.columns.str.replace(' ', '_')


print(df.describe())


print(df['genre'].value_counts())


print(df.corr())

# line for a numeric column
df1=df["budget"]
df2=df["frequency"]
plt.hist(df1,bins=20, edgecolor='black', figsize=(10, 6))
plt.title('Distribution of Budget')
plt.xlabel('Budget')
plt.ylabel('Frequency')
plt.show()

# Assuming the column containing movie ratings is named 'rating'
highest_rated_movie = df[df['rating'] == df['rating'].max()]['movie_title'].values[0]

print("The highest-rated movie is:", highest_rated_movie)

# Assuming there is a column named 'release_year' for movie release year
# Count the number of movies released in 2016
movies_2016_count = df[df['release_year'] == 2016].shape[0]

print(f"The number of movies released in the year 2016 is: {movies_2016_count}")

filtered_df = df[(df['release_year'] >= 2015) & (df['release_year'] <= 2017)]

# Calculate the average revenue for these movies
average_revenue_2015_to_2017 = filtered_df['revenue'].mean()

print(f"The average revenue of movies from 2015 to 2017 is: {average_revenue_2015_to_2017}")

movies_2016_count = df[df['release_year'] == 2016].shape[0]

print(f"The number of movies released in the year 2016 is: {movies_2016_count}")
high_rated_movies_count = df[df['rating'] >= 8.0].shape[0]

print(f"The number of movies with a rating of at least 8.0 is: {high_rated_movies_count}")

# Assuming there is a column named 'Genre' for movie genres
# Split the genres and create a list of all unique genres
unique_genres = df['Genre'].str.split(', ').explode().unique()

# Count the number of unique genres
num_unique_genres = len(unique_genres)

print(f"The number of unique genres in the dataset is: {num_unique_genres}")

