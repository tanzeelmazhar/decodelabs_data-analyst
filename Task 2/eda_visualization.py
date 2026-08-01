"""
DecodeLabs Data Analytics Internship
Project 2: Data Visualization

Author: Tanzeel Mazhar

Description:
This script creates visualizations from the cleaned
e-commerce dataset and automatically saves all charts
inside a folder named 'charts'.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load Cleaned Dataset

FILE_NAME = "Cleaned_Dataset.xlsx"

df = pd.read_excel(FILE_NAME)

print("Dataset Loaded Successfully!")

# Create Charts Folder

os.makedirs("charts", exist_ok=True)

# Chart 1: Top Selling Products

plt.figure(figsize=(10,6))

df["Product"].value_counts().plot(kind="bar")

plt.title("Top Selling Products")
plt.xlabel("Products")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("charts/top_selling_products.png")

plt.close()

# Chart 2: Payment Method Distribution

plt.figure(figsize=(7,7))

df["PaymentMethod"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Payment Method Distribution")

plt.tight_layout()

plt.savefig("charts/payment_method_distribution.png")

plt.close()

# Chart 3: Order Status Distribution

plt.figure(figsize=(8,5))

df["OrderStatus"].value_counts().plot(kind="bar")

plt.title("Order Status Distribution")

plt.xlabel("Order Status")

plt.ylabel("Number of Orders")

plt.tight_layout()

plt.savefig("charts/order_status_distribution.png")

plt.close()

# Chart 4: Total Price Distribution

plt.figure(figsize=(8,5))

plt.hist(df["TotalPrice"], bins=20)

plt.title("Total Price Distribution")

plt.xlabel("Total Price")

plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("charts/total_price_distribution.png")

plt.close()

# Chart 5: Outlier Detection

plt.figure(figsize=(7,5))

plt.boxplot(df["TotalPrice"])

plt.title("Box Plot of Total Price")

plt.ylabel("Total Price")

plt.tight_layout()

plt.savefig("charts/total_price_boxplot.png")

plt.close()

# Chart 6: Top 10 Products

plt.figure(figsize=(10,6))

df["Product"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Products")

plt.xlabel("Products")

plt.ylabel("Orders")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("charts/top_10_products.png")

plt.close()

# ------------------------------------------------------------------
# NEW CHARTS ADDED BELOW
# ------------------------------------------------------------------

# Chart 7: Revenue by Product

plt.figure(figsize=(10,6))

df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False).plot(kind="bar", color="#2a9d8f")

plt.title("Revenue by Product")
plt.xlabel("Products")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("charts/revenue_by_product.png")

plt.close()

# Chart 8: Quantity Sold by Product

plt.figure(figsize=(10,6))

df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).plot(kind="bar", color="#e76f51")

plt.title("Quantity Sold by Product")
plt.xlabel("Products")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("charts/quantity_by_product.png")

plt.close()

# Chart 9: Revenue by Payment Method

plt.figure(figsize=(8,6))

df.groupby("PaymentMethod")["TotalPrice"].sum().sort_values(ascending=False).plot(kind="bar", color="#457b9d")

plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("charts/revenue_by_payment_method.png")

plt.close()

# Chart 10: Referral Source Distribution

plt.figure(figsize=(7,7))

df["ReferralSource"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Referral Source Distribution")

plt.tight_layout()

plt.savefig("charts/referral_source_distribution.png")

plt.close()

# Chart 11: Monthly Sales Trend

plt.figure(figsize=(10,6))

df["Date"] = pd.to_datetime(df["Date"])
monthly_sales = df.set_index("Date").resample("ME")["TotalPrice"].sum()
monthly_sales.plot(kind="line", marker="o", color="#6a4c93")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")

plt.tight_layout()

plt.savefig("charts/monthly_sales_trend.png")

plt.close()

# Chart 12: Items in Cart Distribution

plt.figure(figsize=(8,5))

df["ItemsInCart"].value_counts().sort_index().plot(kind="bar", color="#f4a261")

plt.title("Items in Cart Distribution")
plt.xlabel("Number of Items in Cart")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/items_in_cart_distribution.png")

plt.close()

print("="*50)
print("Charts Generated Successfully!")
print("Saved inside 'charts' folder.")
print("="*50)