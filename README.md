# E-commerce Sales Analysis

## 📊 Overview

This project performs an exploratory data analysis of e-commerce product sales using Python.

The objective is to analyze product performance through sales volume, pricing, revenue, descriptive statistics, correlation analysis, and data visualization.

The project demonstrates a complete introductory Data Science workflow, from data preparation and analysis to business insights.

---

## 🎯 Business Objective

The analysis aims to answer questions such as:

* Which product generates the highest revenue?
* Which product sells the most units?
* How is revenue distributed across products?
* What is the average product price?
* Is there a relationship between product price and sales volume?

---

## 🛠️ Technologies

* Python 3.12
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## 📁 Project Structure

```text
01-ecommerce-sales-analysis/
│
├── data/
│
├── notebooks/
│   └── 01_sales_analysis.ipynb
│
├── reports/
│
├── src/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📈 Analysis Performed

The notebook includes:

* DataFrame creation and manipulation
* Revenue calculation
* Product performance analysis
* Revenue ranking
* Sales volume analysis
* Revenue percentage analysis
* Descriptive statistics
* Correlation analysis
* Scatter plot analysis
* Linear regression trend analysis
* Revenue distribution visualization
* Business KPI analysis

---

## 💰 Key Results

### Total Revenue

**R$ 828,500**

### Highest Revenue Product

**Laptop**

The Laptop generated approximately **65% of total revenue**.

### Best-Selling Product

**Mouse**

The Mouse sold **350 units**, making it the product with the highest sales volume.

### Average Product Price

**R$ 1,404**

---

## 💡 Business Insights

One of the main findings is that the product with the highest sales volume was not the product generating the highest revenue.

The Mouse sold the most units, while the Laptop generated the most revenue.

This demonstrates the importance of analyzing both **sales volume and revenue** when evaluating product performance.

The analysis also identified a negative relationship between product price and units sold in this small dataset.

---

## 📊 Visualizations

The project includes visualizations for:

* Revenue by Product
* Units Sold by Product
* Price vs Units Sold
* Revenue Distribution by Product
* Price vs Sales Trend

These visualizations help transform raw data into actionable business insights.

---

## 📐 Statistical Analysis

The correlation between product price and units sold was approximately:

**-0.56**

This indicates a moderate negative linear relationship within this dataset.

However, the dataset contains only five products, so this result should be interpreted as exploratory rather than statistically conclusive.

The linear regression analysis was also performed as an exploratory exercise to understand the relationship between price and sales volume.

---

## ⚠️ Dataset Limitation

This project uses a small illustrative dataset containing only five products.

Therefore, the findings should not be considered statistically representative of a real e-commerce business.

A larger real-world dataset would be required for:

* Robust statistical analysis
* Reliable predictive modeling
* Customer segmentation
* Demand forecasting
* Pricing optimization

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/bailona/ecommerce-sales-analysis.git
```

Navigate to the project:

```bash
cd ecommerce-sales-analysis
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

Start Jupyter Notebook:

```powershell
jupyter notebook
```

Then open:

```text
notebooks/01_sales_analysis.ipynb
```

---

## 🚀 Future Improvements

Possible extensions for this project include:

* Use a larger real-world e-commerce dataset
* Add customer-level analysis
* Analyze monthly sales trends
* Perform customer segmentation
* Build a sales prediction model
* Add feature engineering
* Compare multiple machine learning algorithms
* Create an interactive dashboard

---

## 👨‍💻 Author

**Paulo Anderson Bailona**

Senior QA Automation Engineer | SDET | Data Science & AI

GitHub: https://github.com/bailona

LinkedIn: https://www.linkedin.com/in/paulo-anderson-b-174127136/
