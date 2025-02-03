import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from collections import Counter, OrderedDict
from IPython.display import Markdown, display

#Wprowadzenie data setu do programu
csv_file = "ostateczny_dataset.csv"
df = pd.read_csv(csv_file)
df = df.drop('track_id',axis = 1)
df = df.drop('Unnamed: 0',axis = 1)

# Wyświetlanie innformacji o datasecie
#df.info()

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

