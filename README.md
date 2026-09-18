# E-commerce Sales Analysis

## Overview

This project performs an exploratory data analysis of e-commerce product sales.

The objective is to analyze product performance using sales volume, product prices, and revenue, identifying relevant business insights through data analysis and visualization.

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Dataset

The current dataset contains information about five products:

- Product
- Units sold
- Price
- Revenue

Revenue was calculated using:

Revenue = Units Sold × Price

## Analysis Performed

The project includes:

- DataFrame creation and manipulation
- Revenue calculation
- Revenue ranking by product
- Units sold analysis
- Revenue percentage analysis
- Descriptive statistics
- Correlation analysis
- Scatter plot analysis
- Linear regression trend analysis
- Revenue distribution visualization

## Key Findings

- Total revenue: R$ 828,500
- Laptop generated the highest revenue.
- Laptop represented approximately 65% of total revenue.
- Mouse was the best-selling product with 350 units sold.
- Average product price: R$ 1,404.
- The analysis showed a negative relationship between price and units sold in this small dataset.

## Important Limitation

This is an exploratory dataset containing only five products.

Therefore, the observed relationships should not be interpreted as statistically conclusive or as a production prediction model.

A larger real-world dataset would be required for more robust statistical analysis and machine learning.

## Project Structure

```text
01-ecommerce-sales-analysis/
│
├── data/
├── notebooks/
│   └── 01_sales_analysis.ipynb
├── reports/
├── src/
├── .venv/
├── requirements.txt
└── README.md

## Author

Paulo Anderson Bailona

Senior QA Automation Engineer | SDET | Data Science & AI