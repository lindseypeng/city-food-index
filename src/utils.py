import ast
import pandas as pd
import ast
import plotly.express as px

def filter_city(df, city):
    return df[df["City"] == city]

def average_rating(df_city):
    return df_city["Rating"].mean()

def median_rating(df_city):
    return df_city["Rating"].median()

def rating_std(df_city):
    return df_city["Rating"].std()

def rating_spread(df_city):
    return df_city["Rating"].max() - df_city["Rating"].min()

def parse_cuisine_list(value):
    if pd.isna(value):
        return []
    
    try:
        parsed = ast.literal_eval(value)
        if isinstance(parsed, list):
            return parsed
        else:
            return []
    except (ValueError, SyntaxError):
        return []


def restaurant_count(df_city):
    return len(df_city)

def total_reviews(df_city):
    return df_city["Number of Reviews"].sum()

def avg_reviews_per_restaurant(df_city):
    return df_city["Number of Reviews"].mean()

def cuisine_diversity(df_city):
    all_cuisines = []

    for cuisines in df_city["Cuisine Style"].dropna():
        all_cuisines.extend(cuisines)

    return len(set(all_cuisines))

def hidden_gem_density(df_city, rating_threshold=4.5, review_threshold=100):
    gems = df_city[
        (df_city["Rating"] >= rating_threshold) &
        (df_city["Number of Reviews"] <= review_threshold)
    ]
    return len(gems) / len(df_city)


def rating_inflation_score(df_city):
    return df_city["Rating"].mean()

def weighted_rating(df_city):
    return (
        (df_city["Rating"] * df_city["Number of Reviews"]).sum()
        / df_city["Number of Reviews"].sum()
    )

def inflation_gap(df_city):
    return average_rating(df_city) - weighted_rating(df_city)

def compute_city_metrics(df_city):
    return {
        "avg_rating": average_rating(df_city),
        "median_rating": median_rating(df_city),
        "rating_std": rating_std(df_city),
        "restaurant_count": restaurant_count(df_city),
        "cuisine_diversity": cuisine_diversity(df_city),
        "avg_reviews": avg_reviews_per_restaurant(df_city),
        "hidden_gem_density": hidden_gem_density(df_city),
        "weighted_rating": weighted_rating(df_city),
        "inflation_gap": inflation_gap(df_city),
    }

def compare_cities(df, city_a, city_b):
    df_a = filter_city(df, city_a)
    df_b = filter_city(df, city_b)

    metrics_a = compute_city_metrics(df_a)
    metrics_b = compute_city_metrics(df_b)

    return {
        "city_a": metrics_a,
        "city_b": metrics_b
    }

def plot_rating_distribution(df, city_a, city_b):
    subset = df[df["City"].isin([city_a, city_b])]
    
    return px.violin(
        subset,
        x="City",
        y="Rating",
        box=True,
        points="all"
    )

def plot_reviews_vs_rating(df, city_a, city_b):
    subset = df[df["City"].isin([city_a, city_b])]

    return px.scatter(
        subset,
        x="Number of Reviews",
        y="Rating",
        color="City",
        log_x=True
    )
