import numpy as np
import pandas as pd


#wczytywanie data setu
df = pd.read_csv('ostateczny_dataset.csv')
df.head()

#usuwanie duplikatów i brakujących wartości
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

#sprawdzanie wymiarów datasetu po oczyszczeniu, wyświetlenia liczby wierszy i kolumn
df.shape

#wyświetlanie liczby wystąpień unikalnych gatunków, sprawdzenie rozkładu
print(df['track_genre'].value_counts())

#liczenie gatunków
num_categories = df['track_genre'].nunique()
num_categories

#usuwanie niepotrzebnych kolumn
columns_to_drop = ['track_name','artists', 'album_name', 'track_id', 'danceability', 'duration_ms', 'explicit',	'loudness',	'acousticness', 'liveness', 'energy', 'speechiness', 'Unnamed:0']
df.drop(columns=[col for col in columns_to_drop if col in df.columns], axis=1, inplace=True)

df.drop(df.columns[0], axis=1, inplace=True)

#opis statystyczny datasetu
df.describe()

#sprawdzenie typów danych
df.dtypes

# Sprawdzenie dostępnych kolumn
print(df.columns)

# Jeśli kolumna 'popularity' istnieje, usuń ją
if 'popularity' in df.columns:
    X = df.drop('popularity', axis=1)  # cechy: wszystkie kolumny oprócz 'popularity'
    y = df['popularity']  # zmienna docelowa: 'popularity'
else:
    print("'popularity' column not found")

    # kodowanie kolumny "track_genre" na wartości numeryczne, sklearn nie akceptuje danych
    # kategorycznych, więc kodujemy 'track_genre'
    from sklearn.preprocessing import LabelEncoder

    le = LabelEncoder()
    df['track_genre'] = le.fit_transform(df['track_genre'])

    # kodowanie kolumny "track_genre" na wartości numeryczne, sklearn nie akceptuje danych
    # kategorycznych, więc kodujemy 'track_genre'
    from sklearn.preprocessing import LabelEncoder

df.head(20)
print()