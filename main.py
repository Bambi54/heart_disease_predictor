import pandas as pd
from import_data import fetch_dataset
from sklearn.model_selection import train_test_split


data = fetch_dataset()

# Wyświetlenie pierwszych kilku wierszy
print("\nPierwsze 5 wierszy danych:")
print(data.head())

train_data, test_data = train_test_split(data, test_size=0.3, random_state=42)