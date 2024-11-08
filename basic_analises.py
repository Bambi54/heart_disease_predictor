import pandas as pd
from import_data import fetch_dataset
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt


data = fetch_dataset()

print("\nPierwsze 5 wierszy danych:")
print(data.head())

train_data, test_data = train_test_split(data, test_size=0.3, random_state=42)


print("\nLiczba brakujących wartości w poszczególnych kolumnach:")
print(data.isnull().sum())

target_column = data.Target
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x=target_column)
plt.title('Rozkład zmiennej docelowej')
plt.xlabel('Wartości docelowe')
plt.ylabel('Częstotliwość')
plt.show()

# macierz korelacji
plt.figure(figsize=(12, 10))
numeric_data = data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_data.corr()
sns.heatmap(correlation_matrix, cmap="coolwarm", fmt=".2f")
plt.title('Macierz korelacji między zmiennymi')
plt.show()

print("\nZbiór treningowy - Podsumowanie statystyczne:")
print(train_data.describe())

print("\nZbiór testowy - Podsumowanie statystyczne:")
print(test_data.describe())