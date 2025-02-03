import pandas as pd
from collections import Counter


#Wprowadzenie data setu do programu
csv_file = "ostateczny_dataset.csv"
df = pd.read_csv(csv_file)
df = df.drop('track_id',axis = 1)
df = df.drop('Unnamed: 0',axis = 1)

""" Opis danych
track_id: float - Identyfikator Spotify dla utworu, który został usunięty

artists: object - Nazwy artystów, którzy wykonali utwór. Jeśli jest więcej niż jeden artysta, są one rozdzielone znakiem ; album_name: object - Nazwa albumu, w którym pojawia się utwór

track_name: object - Nazwa utworu

popularity: integer - Popularność utworu jest wartością w zakresie od 0 do 100, gdzie 100 oznacza największą popularność. Popularność obliczana jest na podstawie algorytmu, który uwzględnia głównie całkowitą liczbę odtworzeń utworu oraz to, jak niedawno miały one miejsce. Generalnie utwory często odtwarzane obecnie będą miały wyższą popularność niż te, które były popularne w przeszłości. Zduplikowane utwory (np. ten sam utwór na singlu i albumie) oceniane są niezależnie. Popularność artysty i albumu jest matematycznie wyprowadzana z popularności utworów. duration_ms: Długość utworu w milisekundach

explicit: bool - Czy utwór zawiera wulgarny język (true = tak, zawiera; false = nie, nie zawiera LUB nieznane)

danceability: float - Wskaźnik "taneczności" opisuje, jak odpowiedni jest utwór do tańczenia, na podstawie kombinacji elementów muzycznych, takich jak tempo, stabilność rytmu, siła bitu i ogólna regularność. Wartość 0.0 oznacza najmniejszą taneczność, a 1.0 największą.

duration_ms : integer - Czas trwania piosenki w milisekundach.

energy: float - Energia to miara w skali od 0.0 do 1.0, która odzwierciedla percepcyjną intensywność i aktywność. Zazwyczaj energetyczne utwory są szybkie, głośne i hałaśliwe. Na przykład death metal ma wysoką energię, podczas gdy preludium Bacha osiąga niską wartość na tej skali.

key: integer - Tonacja, w której znajduje się utwór. Liczby całkowite odpowiadają tonom według standardowego zapisu klasy Pitch Class. Np. 0 = C, 1 = C♯/D♭, 2 = D itd. Jeśli nie wykryto tonacji, wartość wynosi -1.

loudness: float - Ogólna głośność utworu wyrażona w decybelach (dB)

mode: integer - Tryb wskazuje modalność (durowy lub molowy) utworu, czyli typ skali, z której pochodzi jego zawartość melodyczna. Tryb durowy oznaczony jest jako 1, a molowy jako 0.

speechiness: float - Wskaźnik "mówności" wykrywa obecność mówionych słów w utworze. Im bardziej nagranie przypomina wyłącznie mowę (np. audycja, audiobook, poezja), tym bliżej wartości 1.0. Wartości powyżej 0.66 opisują utwory składające się prawdopodobnie w całości z mowy. Wartości od 0.33 do 0.66 odnoszą się do utworów, które mogą zawierać zarówno muzykę, jak i mowę (np. muzyka rapowa). Wartości poniżej 0.33 najprawdopodobniej reprezentują muzykę i inne nagrania bez wyraźnych cech mowy.

acousticness: float - Miara pewności w skali od 0.0 do 1.0, czy utwór jest akustyczny. Wartość 1.0 oznacza wysoką pewność, że utwór jest akustyczny.

instrumentalness: float - Przewiduje, czy utwór nie zawiera wokali. Dźwięki "ooh" i "aah" traktowane są jako instrumentalne w tym kontekście. Utwory rapowe lub mówione są wyraźnie "wokalne". Im bliższa wartości 1.0 jest instrumentalność, tym większe prawdopodobieństwo, że utwór nie zawiera wokalu.

liveness: float - Wykrywa obecność publiczności w nagraniu. Wyższe wartości liveness wskazują na zwiększone prawdopodobieństwo, że utwór był wykonywany na żywo. Wartość powyżej 0.8 silnie sugeruje, że utwór jest nagraniem na żywo.

valence: float - Miara w skali od 0.0 do 1.0 opisująca muzyczną pozytywność utworu. Utwory o wysokiej wartości valence brzmią bardziej pozytywnie (np. wesołe, radosne, euforyczne), natomiast utwory o niskiej wartości brzmią bardziej negatywnie (np. smutne, przygnębione, gniewne).

tempo: float - Szacowane tempo utworu wyrażone w uderzeniach na minutę (BPM). W terminologii muzycznej tempo to szybkość lub rytm utworu, który bezpośrednio wynika z średniego czasu trwania bitu.

time_signature: integer - Szacowany metrum utworu. Metrum (podział rytmiczny) to konwencja notacyjna określająca, ile bitów znajduje się w każdym takcie. Wartości wynoszą od 3 do 7, co odpowiada metrum od 3/4 do 7/4.

track_genre: object - Gatunek muzyczny, do którego należy utwór.

W przypadku zmiennych key oraz tempo, konieczne będzie użycie techniki One Hot Encoding, w celu zapisu ich jako zmienne binarne."""

# Wyświetlanie innformacji o datasecie
df.info()
df.head()

# Removing duplicated
counter = Counter(df['track_name'])
if len(Counter({k: c for k, c in counter.items() if c > 1})) != 0:
  df = df.drop_duplicates(subset='track_name')
  df = df.reset_index(drop=True)


# Removing songs longer than 10 min. 
# They are likely not a single song, but a compilation of many
df = df.loc[df["duration_ms"] < 10*60000]


# Removing songs with a large value of speechiness
# They are likely a podcast or a recitation
df = df.loc[df["speechiness"] < 0.66]


# Removing songs with assigned time signature of 0 and 1
# Music theory does not allow a time signature of 0; this is likely a mistake by the dataset authors
# While a time signature of 1 is theoretically possible, it is very unlikely for this value to be intentional
df.drop(df[ df['time_signature'] == 1 ].index, inplace = True)
df.drop(df[ df['time_signature'] == 0 ].index, inplace = True)
Counter(df['time_signature'])

# Wyświetlenie ile piosenek zostało usuniętych
df.info()

# Ile mamy zmiennych kategorycznych
Counter(df['time_signature'])
Counter(df['mode'])

# For clearer presentation, values of the 'key' parameter {0, 1, ..., 11} should be replaced with the corresponding musical note names
key_mapping = {
    0: 'C', 1: 'C♯/D♭', 2: 'D', 3: 'D♯/E♭', 4: 'E', 5: 'F',
    6: 'F♯/G♭', 7: 'G', 8: 'G♯/A♭', 9: 'A', 10: 'A♯/B', 11: 'H'
}
df['key'] = df['key'].replace(key_mapping)


# It's useful to analyze musical scales; they consist of a key and a mode - minor or major
# For better readability the minor scales will be written in lower case
def format_key(row):
    if row['mode'] == 0:  # moll
        return row['key'].lower()
    else:  # dur
        return row['key']

# Apply the transformation
df['key_mode'] = df.apply(format_key, axis=1)

mode_mapping = {0: '-moll', 1: '-dur'}

# Poniżej widzimy, że mamy w datasecie zmienne kategoryczne: key, audio_mode i time_signature.
df.describe()

