# Airbnb Pricing Strategy Analysis

##  Project Overview
This project analyzes Airbnb listing data to identify factors that influence pricing.
The goal is to support pricing strategy optimization using data analysis and visualization.

---

##  Dataset
- Source: Airbnb Open Data
- Rows: ~102,000
- Columns: 26

Main features:
- price
- room type
- neighbourhood
- neighbourhood group
- availability 365
- minimum nights
- number of reviews

---

##  Tools & Technologies
- Python
- Pandas
- Matplotlib
- Seaborn
- Tableau / Power BI (for visualization)
- Git & GitHub

---

##  Data Cleaning
- Removed missing and invalid prices
- Converted price column to numeric
- Removed prices ≤ 0
- Handled missing values in key columns
- Identified inconsistent categorical values

---

##  Analysis Performed
- Descriptive statistics of prices
- Average price by room type
- Top 10 most expensive neighbourhoods
- Correlation analysis between numerical features
- Exploration of categorical variables

---

##  Visualizations
- Bar chart: Average price by room type
- Bar chart: Top 10 neighbourhoods by price
- Correlation heatmap

---

##  Key Insights
- Room type strongly impacts price
- Entire homes/apartments are the most expensive
- Location significantly affects pricing
- Number of reviews does not directly imply higher price
- Availability and minimum nights influence pricing strategy

---

##  Next Steps
- Advanced outlier detection
- Time-based analysis using review dates
- Interactive dashboards in Tableau / Power BI
- Price prediction model (machine learning)

## How to run the project
```bash
pip install -r requirements.txt
python analysis.py

---

##  Author
**Szymon Wypler**

Junior Data Analyst / Data Science Enthusiast
