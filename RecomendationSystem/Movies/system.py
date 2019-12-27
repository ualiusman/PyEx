import numpy as num
import pandas as pd




ratings_data = pd.read_csv("ratings.csv")


movie_names = pd.read_csv("movies.csv")


movie_data = pd.merge(ratings_data,movie_names,on="movieId")
ratings_mean_count = pd.DataFrame(movie_data.groupby("title")["rating"].mean())
ratings_mean_count["ratings_count"] = pd.DataFrame(movie_data.groupby("title")["rating"].count()) 

user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')




forrest_gump_ratings = user_movie_rating['Forrest Gump (1994)']
movies_like_forest_gump = user_movie_rating.corrwith(forrest_gump_ratings)

corr_forrest_gump = pd.DataFrame(movies_like_forest_gump, columns=['Correlation'])
corr_forrest_gump.dropna(inplace=True)
print(corr_forrest_gump.head())