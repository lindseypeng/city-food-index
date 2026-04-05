import streamlit as st
from src.load_data import load_ta_restaurants
from src.utils import compare_cities, plot_rating_distribution, plot_reviews_vs_rating

st.title("Asian Food City Comparison")
st.write("Compare restaurant ratings and cuisine diversity between two cities.")

@st.cache_data
def get_data():
    return load_ta_restaurants()

df = get_data()
cities = sorted(df["City"].dropna().unique())

col1, col2 = st.columns(2)
with col1:
    city_a = st.selectbox("City A", cities, index=cities.index("Amsterdam") if "Amsterdam" in cities else 0)
with col2:
    city_b = st.selectbox("City B", cities, index=cities.index("Paris") if "Paris" in cities else 1)

if city_a == city_b:
    st.warning("Please select two different cities.")
    st.stop()

metrics = compare_cities(df, city_a, city_b)
m_a = metrics["city_a"]
m_b = metrics["city_b"]

st.divider()

st.subheader("At a glance")
cols = st.columns(4)

def delta(a, b):
    return f"{a - b:+.2f}"

cols[0].metric(f"Avg Rating — {city_a}", f"{m_a['avg_rating']:.2f}", delta(m_a['avg_rating'], m_b['avg_rating']))
cols[1].metric(f"Avg Rating — {city_b}", f"{m_b['avg_rating']:.2f}")
cols[2].metric(f"Restaurants — {city_a}", m_a['restaurant_count'])
cols[3].metric(f"Restaurants — {city_b}", m_b['restaurant_count'])

cols2 = st.columns(4)
cols2[0].metric(f"Weighted Rating — {city_a}", f"{m_a['weighted_rating']:.2f}")
cols2[1].metric(f"Weighted Rating — {city_b}", f"{m_b['weighted_rating']:.2f}")
cols2[2].metric(f"Hidden Gems — {city_a}", f"{m_a['hidden_gem_density']:.1%}")
cols2[3].metric(f"Hidden Gems — {city_b}", f"{m_b['hidden_gem_density']:.1%}")

cols3 = st.columns(4)
cols3[0].metric(f"Inflation Gap — {city_a}", f"{m_a['inflation_gap']:.3f}")
cols3[1].metric(f"Inflation Gap — {city_b}", f"{m_b['inflation_gap']:.3f}")
cols3[2].metric(f"Cuisine Diversity — {city_a}", m_a['cuisine_diversity'])
cols3[3].metric(f"Cuisine Diversity — {city_b}", m_b['cuisine_diversity'])

st.divider()

st.subheader("Rating Distribution")
st.plotly_chart(plot_rating_distribution(df, city_a, city_b), use_container_width=True)

st.subheader("Reviews vs Rating")
st.plotly_chart(plot_reviews_vs_rating(df, city_a, city_b), use_container_width=True)
