import pandas as pd
"""

Splitting of Main Datasets for easy use ahead,
Main Dataset -
    Name - 25k IMDb Movie Datasets (https://www.kaggle.com/datasets/utsh0dey/25k-movie-dataset)
    User - UTSHO DEY (https://www.kaggle.com/utsh0dey)

"""

main_data = pd.read_csv("assets/Movie_Dataset.csv")

# Typos in real dataset renaming and saving new one with corrected names
main_data.rename(columns= {
    "movie title": "Movies",
    "Generes": "Genres",
    "Plot Kyeword": "Keywords",
    "Top 5 Casts": "Top Casts",
}, inplace=True)
print(main_data.iloc[0,:])

print()

# Splitting for the Ratings Data
rating_data = main_data.loc[:, ["Movies", "Rating", "User Rating"]]
print(rating_data.loc[0, :])

print()

# Splitting for the Keywords Data
keywords_data = main_data.loc[:, ["Movies", "Keywords", "Top Casts", "Director"]]
print(keywords_data.loc[0, :])

print()

# Splitting for the Genres Data
genres_data = main_data.loc[:, ["Movies", "Genres"]]
print(genres_data.loc[0,:])


# One time run to create files
# Run again if changes are made in any columns
# main_data.to_csv("assets/main_data.csv", index=False)
# rating_data.to_csv("assets/ratings.csv", index=False, header=None)
# keywords_data.to_csv("assets/keywords.csv", index=False, header=None)
# genres_data.to_csv("assets/genres.csv", index=False, header=None)

