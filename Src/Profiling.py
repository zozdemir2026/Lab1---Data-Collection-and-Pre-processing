import pandas as pd


def profile_transactions(transactions):
    prices = pd.to_numeric(transactions["price"], errors="coerce")
    cities = set(transactions["shipping_city"].dropna())

    print("Minimum price:", prices.min())
    print("Average price:", round(prices.mean(), 2))
    print("Maximum price:", prices.max())
    print("Number of unique cities:", len(cities))