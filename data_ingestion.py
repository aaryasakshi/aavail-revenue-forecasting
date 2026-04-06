import pandas as pd

def load_data():
    data = pd.DataFrame({
        "country": ["USA", "UK"],
        "revenue": [100, 200]
    })
    return data
