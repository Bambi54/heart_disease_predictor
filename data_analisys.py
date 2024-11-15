import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport
from import_data import fetch_dataset


data = fetch_dataset()

print("Informacje o danych:")
data.info()

print("\nPodgląd danych:")
print(data.head())

missing_data = data.isnull().sum()
print("\nLiczba brakujących wartości w każdej kolumnie:")
print(missing_data)

print("\nStatystyki opisowe danych:")
print(data.describe(include="all"))

# Rozkłady zmiennych numerycznych
plt.figure(figsize=(10, 6))
data.hist(bins=20, figsize=(15, 10), color='blue', alpha=0.7)
plt.suptitle('Histogramy zmiennych numerycznych')
plt.show()


# Rozkłady zmiennych kategorycznych
categorical_columns = data.select_dtypes(include=['object']).columns
for col in categorical_columns:
    plt.figure(figsize=(8, 6))
    sns.countplot(x=data[col])
    plt.title(f'Rozkład zmiennej kategorycznej: {col}')
    plt.show()


# Macierz korelacji
plt.figure(figsize=(12, 10))
numeric_data = data.select_dtypes(include=['float64', 'int64'])
sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Macierz korelacji zmiennych numerycznych")
plt.show()

# Generowanie raportu z Pandas Profiling
profile = ProfileReport(data, title="Raport Pandas Profiling", explorative=True)
profile.to_file("EDA_report.html")
