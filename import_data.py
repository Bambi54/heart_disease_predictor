from ucimlrepo import fetch_ucirepo
import pandas as pd

def fetch_dataset():
    data = fetch_ucirepo(id=697)
    return pd.concat([data.features, data.targets], axis=1)