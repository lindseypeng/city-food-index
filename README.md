# City Food Index

A Streamlit app that compares the restaurant scenes of two cities — like a cost-of-living index, but for food.

## What it does

- Loads restaurant data from TripAdvisor (TA_restaurants_curated.csv)
- Select any two cities to compare side by side
- Shows key metrics: average rating, weighted rating, hidden gem density, cuisine diversity, rating inflation gap
- Visualizes rating distributions and reviews vs rating

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
