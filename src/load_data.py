import pandas as pd

def load_restaurants(path="data/restaurants.csv"):
    df = pd.read_csv(path)
    return df
