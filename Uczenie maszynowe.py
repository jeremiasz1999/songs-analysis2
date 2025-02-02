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