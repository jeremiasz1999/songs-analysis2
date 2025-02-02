import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


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

    le = LabelEncoder()
    X_train['genre'] = le.fit_transform(X_train['genre'])
    X_test['genre'] = le.transform(X_test['genre'])  # Używamy tylko `transform` dla danych testowych
    # df.head(20)
    # podział danych i trenowanie model

    # podział danych i trenowanie modelu
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor

    # oddzielenie cech (x) od zmiennej docelowej (y)
    X = df.drop('popularity', axis=1)  # cechy: wszytskie kolumny poza popularity
    y = df['popularity']  # zmienna docelowa: popularity

    # podział na dane treningowe i testowe
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # inicjalizacaj modelu Random Forest
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    # trenowanie modelu na danych treningowych
    rf.fit(X_train, y_train)

    # przewidywanie wyników danych testowych
    y_pred = rf.predict(X_test)
    print(type(y_test))
    print(y_test[:5])  # Podgląd pierwszych 5 wartości
