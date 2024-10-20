# %% 

import pandas as pd

df = pd.read_csv("aoty.csv")

df.head()

# %%

# Dropping album links because won't need it for analysis

df1 = df.drop("album_link", axis=1)

df1.head()

# %%

# Some issues:
# - Genres are strings, need to turn it into a list or if you need it, hash maps to work with
# - Exact day isn't that important but year and month is, so we need to separate them
# - ratings are strings and have "ratings" word in it. Need to turn them into integers

# Making months and years a different columns

df1['release_date'] = pd.to_datetime(df1['release_date'], format='mixed')

df1['Month'] = df1['release_date'].dt.strftime('%B')
df1['Year'] = df1['release_date'].dt.year

# Making genres strings lists of genres

df1['genres'] = df1['genres'].apply(lambda x: [genre.strip() for genre in x.split(',')])

# Deleting " ratings" from ratings

df1['rating_count'] = df['rating_count'].str.replace(' ratings', '').str.replace(',', '').astype(int)

# %%

# Gathering rows with unknown in it
# Luckily most of them are in names and there are only a few exceptions

df1[df1.apply(lambda row: row.astype(str).str.contains('Unknown').any(), axis=1)]

# %%

df1.to_csv('aoty_processed.csv')
