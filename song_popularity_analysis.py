import numpy as np
import pandas as pd

#Wprowadzenie data setu do programu
csv_file = "ostateczny_dataset.csv"
df = pd.read_csv(csv_file)
df = df.drop('track_id',axis = 1)
df = df.drop('Unnamed: 0',axis = 1)