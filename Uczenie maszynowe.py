import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter, OrderedDict
from IPython.display import Markdown, display


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
Counter(df['time_signature'])

Counter(df['mode'])

key_mapping = {
    0: 'C', 1: 'C♯/D♭', 2: 'D', 3: 'D♯/E♭', 4: 'E', 5: 'F',
    6: 'F♯/G♭', 7: 'G', 8: 'G♯/A♭', 9: 'A', 10: 'A♯/B', 11: 'H'
}
df['key'] = df['key'].replace(key_mapping)
Counter(df['key'])

def format_key(row):
    if row['mode'] == 0:  # moll
        return row['key'].lower()
    else:  # dur
        return row['key']

# Apply the transformation
df['key_mode'] = df.apply(format_key, axis=1)

mode_mapping = {0: '-moll', 1: '-dur'}

#df['key_mode'] = df['key']  + df['mode']
Counter(df['key_mode'])

#usuwanie niepotrzebnych kolumn
columns_to_drop = ['key', 'mode', 'time_signature']
df.drop(columns=[col for col in columns_to_drop if col in df.columns], axis=1, inplace=True)
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

    # kodowanie kolumny "key_mode" na wartości numeryczne, sklearn nie akceptuje danych
    # kategorycznych, więc kodujemy 'key_mode'
    from sklearn.preprocessing import LabelEncoder

    le = LabelEncoder()
    df['key_mode'] = le.fit_transform(df['key_mode'])
    df.head(20)
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


    # obliczanie i wyświetlanie metryk ewaluacyjnych
    mse = mean_squared_error(y_test, y_pred)  # średni błąd kwadratowy (MSE)
    print('mse: ', mse)
    print('r2s: ', r2_score(y_test, y_pred))  # współczynnik determinacji (r^2)

    # obliczanie i wyświetlanie pierwiasta z MSE (RMSE)
    rmse = np.sqrt(mse)
    print('rmse: ', rmse)

    # wykres słupkowy porównujący rzeczywiste wartości z przewidywaniami
    plt.bar(range(len(y_test)), y_test, color='blue', alpha=0.5, label='True Values')  # słupki dla rzeczywistych danych
    plt.bar(range(len(y_pred)), y_pred, color='orange', alpha=0.5, label='Predictions')  # słupki dla przewidywań

    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.legend(loc="upper right")
    plt.show()

    # ważnosc cech
    importances = rf.feature_importances_
    indices = np.argsort(importances)[::-1]

    # wyswietlanie ważności cech w kolejności
    for f in range(X.shape[1]):
        print(f'{X.columns[indices[f]]}: {importances[indices[f]]}')

     # histogram zmiennej 'popularity'
    f['popularity'].hist(bins=50)