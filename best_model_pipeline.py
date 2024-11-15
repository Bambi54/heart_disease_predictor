import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from tpot.export_utils import set_param_recursive
from import_data import fetch_dataset
from sklearn.metrics import classification_report, accuracy_score

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
tpot_data = fetch_dataset()
features = tpot_data.drop('Target', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['Target'], random_state=42)

# Average CV score on the training set was: 0.7829569023919956
exported_pipeline = make_pipeline(
    StandardScaler(),
    RandomForestClassifier(bootstrap=False, criterion="entropy", max_features=0.35000000000000003, min_samples_leaf=1, min_samples_split=7, n_estimators=100)
)
# Fix random state for all the steps in exported pipeline
set_param_recursive(exported_pipeline.steps, 'random_state', 42)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)

print("Raport klasyfikacji:")
print(classification_report(testing_target, results))

accuracy = accuracy_score(testing_target, results)
print(f"\nDokładność modelu na zbiorze testowym: {accuracy:.2f}")
