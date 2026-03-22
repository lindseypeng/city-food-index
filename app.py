import streamlit as st
from src.load_data import load_restaurants
from src.scoring import add_scores
from src.filters import filter_by_query

st.title("Niche Asian Food Finder")
st.write("Find the best Asian restaurants in Berlin by dish or cuisine.")

query = st.text_input("Search by dish or cuisine (e.g. ramen, Vietnamese, dumplings)")

df = load_restaurants()
df = add_scores(df)
results = filter_by_query(df, query)

if results.empty:
    st.warning("No restaurants found. Try a different search.")
else:
    st.dataframe(
        results[["name", "cuisine", "dishes", "score", "price_range"]],
        use_container_width=True,
        hide_index=True,
    )
