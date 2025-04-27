import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

from data_preprocessing import load_and_clean_data

def train():
    data = load_and_clean_data('data/usage_data.csv')
    X = data[['screen_time', 'app_opens', 'social_media_time']]
    y = data['risky_behavior']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    joblib.dump(model, 'src/phone_addiction_model.pkl')

if __name__ == "__main__":
    train()
