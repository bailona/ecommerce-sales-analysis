import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

reports = Path("reports")
reports.mkdir(exist_ok=True)

data = {
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset"],
    "sales": [120, 350, 200, 80, 150],
    "price": [4500, 120, 250, 1800, 350]
}

df = pd.DataFrame(data)

df["revenue"] = df["sales"] * df["price"]

# 1. Revenue by Product
plt.figure(figsize=(10, 5))
plt.bar(df["product"], df["revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (R$)")
plt.savefig(reports / "revenue_by_product.png", dpi=150, bbox_inches="tight")
plt.close()

# 2. Units Sold by Product
plt.figure(figsize=(10, 5))
plt.bar(df["product"], df["sales"])
plt.title("Units Sold by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.savefig(reports / "units_sold_by_product.png", dpi=150, bbox_inches="tight")
plt.close()

# 3. Price vs Units Sold
x = df["price"]
y = df["sales"]

slope, intercept = np.polyfit(x, y, 1)

plt.figure(figsize=(10, 6))
plt.scatter(x, y)

for i, product in enumerate(df["product"]):
    plt.annotate(
        product,
        (x.iloc[i], y.iloc[i]),
        xytext=(8, 5),
        textcoords="offset points"
    )

x_line = np.linspace(x.min(), x.max(), 100)
y_line = slope * x_line + intercept

plt.plot(x_line, y_line)
plt.title("Price vs Units Sold")
plt.xlabel("Price (R$)")
plt.ylabel("Units Sold")
plt.savefig(reports / "price_vs_sales.png", dpi=150, bbox_inches="tight")
plt.close()

# 4. Revenue Distribution
plt.figure(figsize=(8, 8))
plt.pie(
    df["revenue"],
    labels=df["product"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Revenue Distribution by Product")
plt.savefig(reports / "revenue_distribution.png", dpi=150, bbox_inches="tight")
plt.close()

print("Charts generated successfully!")
