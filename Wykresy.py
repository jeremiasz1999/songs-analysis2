from song_popularity_analysis import df
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns


# Dividing parameters into numerical and categorical
cat = df[["key","mode", "time_signature", "key_mode"]].copy()
num = df.drop(["key","mode", "time_signature", "valence", "loudness"], axis = 1)

# ///////////////////////////////// Wykresy zmiennych ciągłych \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Tworzymy wykres o rozmiarze (30, 30) i jedną oś (ax)
fig, ax = plt.subplots(figsize=(30, 30))
num.hist(ax=ax)
plt.show()


# ////////////////////////////// Wykresy zmiennych kategorycznych \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
key_mode_counts = df['key_mode'].value_counts()
colors = ['red' if key.isupper() else 'blue' for key in key_mode_counts.index]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (15,5))
#-------------------------------------------------------------------------------------------------
cat["key_mode"].value_counts().plot(kind='bar', ax = ax1, title = "Key Mode", color=colors)
moll_patch = mpatches.Patch(color='blue', label='moll (minor)')
dur_patch = mpatches.Patch(color='red', label='dur (major)')
ax1.legend(handles=[moll_patch, dur_patch], loc='upper right')
#-------------------------------------------------------------------------------------------------
cat["time_signature"].value_counts().plot(kind='bar', ax = ax2, title = "Time signature")
cat["mode"].value_counts().plot(kind='bar', ax = ax3, title = "audio mode")
plt.show()


# //////////////////////////////\//////Macierz korelacji\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

correlation_matrix=df[['popularity', 'duration_ms', 'acousticness',
                       'danceability', 'energy', 'instrumentalness',
                       'liveness', 'loudness', 'speechiness', 'tempo',
                       'valence']].corr()

plt.figure(figsize=(12,10))
ax = sns.heatmap(correlation_matrix, annot=True, cmap='RdBu_r')
ax.xaxis.tick_top()
plt.xticks(rotation=90)
plt.show()
