import pandas as pd
from src.utils import parse_cuisine_list

def load_restaurants(path="data/onlineData/TA_restaurants_curated.csv"):
    df = pd.read_csv(path)
    df["Cuisine List"] = df["Cuisine Style"].apply(parse_cuisine_list)
    return df

def load_ta_restaurants(path="data/onlineData/TA_restaurants_curated.csv"):
    df = pd.read_csv(path)
    df["Cuisine List"] = df["Cuisine Style"].apply(parse_cuisine_list)
    df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
    df["Number of Reviews"] = pd.to_numeric(df["Number of Reviews"], errors="coerce").fillna(0).astype(int)
    return df



