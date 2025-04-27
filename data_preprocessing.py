import pandas as pd

def load_and_clean_data(filepath):
    data = pd.read_csv(filepath)
    # Basic cleaning (if needed)
    data.dropna(inplace=True)
    return data
