import pandas as pd

def alert():
    data = pd.read_csv('data/predictions.csv')
    risky_days = data[data['Prediction'] == 1]
    for _, row in risky_days.iterrows():
        print(f"Warning: High screen time detected on {row['date']}. Consider taking a break!")

if __name__ == "__main__":
    alert()
