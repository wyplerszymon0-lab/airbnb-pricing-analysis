# ============================================
# Project: Airbnb Pricing Strategy Optimization
# Author: Szymon Wypler
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load data
# -----------------------------
df = pd.read_csv("data/Airbnb_Open_Data.csv", low_memory=False)

print("Preview of the dataset:")
print(df.head())

print("\nDataset info:")
print(df.info())

# -----------------------------
# 2. Data cleaning
# -----------------------------

# Remove rows without price
df = df.dropna(subset=["price"])

# Convert price to numeric
df["price"] = (
    df["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Remove invalid prices
df = df[df["price"] > 0]

# -----------------------------
# 3. Check categorical values
# -----------------------------
print("\nRoom type distribution:")
print(df["room type"].value_counts())

print("\nNeighbourhood group distribution:")
print(df["neighbourhood group"].value_counts())

# -----------------------------
# 4. Descriptive statistics
# -----------------------------
print("\nPrice statistics:")
print(df["price"].describe())

# -----------------------------
# 5. Price analysis by room type
# -----------------------------
room_price = df.groupby("room type")["price"].mean().sort_values()

plt.figure()
room_price.plot(kind="bar")
plt.title("Average price by room type")
plt.ylabel("Price")
plt.xlabel("Room type")
plt.tight_layout()
plt.show()

# -----------------------------
# 6. Top 10 most expensive neighbourhoods
# -----------------------------
top_neighbourhoods = (
    df.groupby("neighbourhood")["price"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure()
top_neighbourhoods.plot(kind="bar")
plt.title("Top 10 most expensive neighbourhoods")
plt.ylabel("Price")
plt.xlabel("Neighbourhood")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# -----------------------------
# 7. Correlation analysis
# -----------------------------
numeric_cols = [
    "price",
    "minimum nights",
    "number of reviews",
    "availability 365",
    "review rate number"
]

corr = df[numeric_cols].corr()

plt.figure()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation heatmap")
plt.tight_layout()
plt.show()

# -----------------------------
# 8. Conclusions
# -----------------------------
print("\nCONCLUSIONS:")
print("- Room type has a strong impact on price (entire homes are the most expensive).")
print("- Location significantly differentiates prices between neighbourhoods.")
print("- A higher number of reviews does not always mean higher prices.")
print("- Availability and minimum nights influence pricing strategy.")
