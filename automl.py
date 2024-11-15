from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
from import_data import fetch_dataset
from sklearn.preprocessing import LabelEncoder


label_encoder = LabelEncoder()
data = fetch_dataset()

data['Target'] = label_encoder.fit_transform(data['Target'])

X = data.drop(columns=['Target'])
y = data['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

tpot = TPOTClassifier(generations=5, population_size=50, verbosity=2, random_state=42)
tpot.fit(X_train, y_train)

print("\nNajlepszy model według TPOT:")
print(tpot.fitted_pipeline_)

accuracy = tpot.score(X_test, y_test)
print(f"\nDokładność modelu na zbiorze testowym: {accuracy:.2f}")

tpot.export("best_model_pipeline.py")
