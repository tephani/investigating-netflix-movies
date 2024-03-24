import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("netflix_data.csv")
# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]
# Select only the columns of interest
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]
# Filter for durations shorter than 60 minutes
short_movies = netflix_movies[netflix_movies.duration < 60]

colors = []
for label, row in netflix_movies.iterrows() :
    if row["genre"] == "Children" :
        colors.append("blue")
    elif row["genre"] == "Documentaries" :
        colors.append("green")
    elif row["genre"] == "Stand-Up":
        colors.append("yellow")
    else:
        colors.append("grey")
            
colors[:10]

fig = plt.figure(figsize=(12,8))

# Scatter plot of duration versus release_year
plt.scatter(netflix_movies.release_year, netflix_movies.duration, c=colors)
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.show()

# Are we certain that movies are getting shorter?
answer = "no"