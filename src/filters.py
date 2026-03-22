def filter_by_query(df, query):
    """Filter restaurants by dish name or cuisine (case-insensitive)."""
    if not query:
        return df
    q = query.lower()
    match = (
        df["cuisine"].str.lower().str.contains(q) |
        df["dishes"].str.lower().str.contains(q)
    )
    return df[match]
