# List of column names to include in new dataframe
cols_ubi = [
    "month",
    "Futurology_universalbasicincome",
    "technology_universalbasicincome",
    "science_universalbasicincome",
    "askscience_universalbasicincome",
    "books_universalbasicincome",
    "scifi_universalbasicincome",
    "movies_universalbasicincome",
    "gaming_universalbasicincome",
    "worldnews_universalbasicincome",
    "news_universalbasicincome",
    "politics_universalbasicincome",
    "AskReddit_universalbasicincome",
]

# Create new dataframe with NaN values filled in with 0, and the index set to the month column
df_ubi = df_main[cols_ubi].fillna(value=0)

df_ubi.head()
