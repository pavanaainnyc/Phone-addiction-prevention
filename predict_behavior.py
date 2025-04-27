import pandas as pd
import joblib

from data_preprocessing import load_and_clean_data

def predict():
    model = joblib.load('src/phone_addiction_model.pkl')
    new_data = load_and_clean_data('data/usage_data.csv')

    X_new = new_data[['screen_time', 'app_opens', 'social_media_time']]
    predictions = model.predict(X_new)

    new_data['Prediction'] = predictions
    new_data.to_csv('data/predictions.csv', index=False)

if __name__ == "__main__":
    predict()
