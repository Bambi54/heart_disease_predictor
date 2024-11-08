from ucimlrepo import fetch_ucirepo
import pandas as pd

def fetch_dataset():
    uciml_data = fetch_ucirepo(id=697)
    return pd.concat([uciml_data.data.features, uciml_data.data.targets], axis=1)