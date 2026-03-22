# Niche Asian Food Finder

A simple Streamlit app that recommends Asian restaurants in Berlin based on dish or cuisine search, using adjusted scoring instead of raw Google ratings.

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

## How it works

- Load restaurant data from `data/restaurants.csv`
- User types a dish or cuisine (e.g. "ramen", "Vietnamese")
- Results are ranked by an adjusted score that accounts for rating and number of reviews
