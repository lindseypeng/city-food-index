def adjusted_score(google_rating, num_reviews):
    """Adjust rating to penalize places with very few reviews."""
    weight = num_reviews / (num_reviews + 50)
    return round(google_rating * weight, 2)

def add_scores(df):
    df = df.copy()
    df["score"] = df.apply(
        lambda row: adjusted_score(row["google_rating"], row["num_reviews"]), axis=1
    )
    return df.sort_values("score", ascending=False)
