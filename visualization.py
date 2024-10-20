# %%

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%

df = pd.read_csv('aoty_processed.csv')

# %%

plt.figure(figsize=(10, 6))
sns.histplot(df['user_score'], bins=20, kde=True)
plt.title('Distribution of User Scores')
plt.xlabel('User Score')
plt.ylabel('Frequency')
plt.show()

# %%

average_score_per_year = df.groupby('Year')['user_score'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='user_score', data=average_score_per_year)
plt.title('Average User Score by Year')
plt.xlabel('Year')
plt.ylabel('Average User Score')
plt.show()

# %%

genre_counts = df['genres'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=genre_counts.values, y=genre_counts.index)
plt.title('Top 10 Genres by Number of Albums')
plt.xlabel('Number of Albums')
plt.ylabel('Genre')
plt.show()


# %%

monthly_releases = df['Month'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x=monthly_releases.index, y=monthly_releases.values)
plt.title('Number of Albums Released by Month')
plt.xlabel('Month')
plt.ylabel('Number of Albums')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.show()

# %%

top_artists = df.groupby('artist').size().nlargest(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_artists.values, y=top_artists.index)
plt.title('Top 10 Artists by Number of Albums')
plt.xlabel('Number of Albums')
plt.ylabel('Artist')
plt.show()
# %%

df_exploded = df.explode('genres')
average_score_by_genre = df_exploded.groupby('genres')['user_score'].mean().reset_index()
top_10_genres = average_score_by_genre.nlargest(10, 'user_score')
plt.figure(figsize=(12, 6))
sns.barplot(x='user_score', y='genres', data=top_10_genres, palette='viridis')
plt.title('Top 10 Genres by Average User Score')
plt.xlabel('Average User Score')
plt.ylabel('Genre')
plt.show()
