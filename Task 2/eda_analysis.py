"""
DecodeLabs Data Analytics Internship
Project 2: Exploratory Data Analysis (EDA)

Author: Tanzeel Mazhar

Description:
This script performs Exploratory Data Analysis (EDA)
on the cleaned e-commerce dataset by calculating
descriptive statistics, identifying trends,
detecting outliers, and generating business insights.
"""

import pandas as pd

# Load Cleaned Dataset

FILE_NAME = "Cleaned_Dataset.xlsx"

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 60)

# Read Dataset
df = pd.read_excel(FILE_NAME)

print("\nDataset Loaded Successfully!")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# Dataset Information

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

df.info()

# Missing Values

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

# Descriptive Statistics

print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)

print(df.describe())

# Mean

print("\nMean Values")
print("Quantity    :", round(df["Quantity"].mean(), 2))
print("Unit Price  :", round(df["UnitPrice"].mean(), 2))
print("Total Price :", round(df["TotalPrice"].mean(), 2))

# Median

print("\nMedian Values")
print("Quantity    :", df["Quantity"].median())
print("Unit Price  :", df["UnitPrice"].median())
print("Total Price :", df["TotalPrice"].median())

# Mode

print("\nMode Values")
print(df[["Quantity", "UnitPrice", "TotalPrice"]].mode())

# Minimum & Maximum

print("\nMinimum Values")
print(df[["Quantity", "UnitPrice", "TotalPrice"]].min())

print("\nMaximum Values")
print(df[["Quantity", "UnitPrice", "TotalPrice"]].max())

# Product Analysis

print("\n" + "=" * 60)
print("TOP SELLING PRODUCTS")
print("=" * 60)

print(df["Product"].value_counts())

# Payment Method Analysis

print("\n" + "=" * 60)
print("PAYMENT METHOD DISTRIBUTION")
print("=" * 60)

print(df["PaymentMethod"].value_counts())

# Order Status Analysis

print("\n" + "=" * 60)
print("ORDER STATUS DISTRIBUTION")
print("=" * 60)

print(df["OrderStatus"].value_counts())

# Revenue Analysis

print("\n" + "=" * 60)
print("REVENUE ANALYSIS")
print("=" * 60)

total_revenue = df["TotalPrice"].sum()
average_revenue = df["TotalPrice"].mean()

print("Total Revenue   :", round(total_revenue, 2))
print("Average Revenue :", round(average_revenue, 2))

# Outlier Detection (IQR Method)

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["TotalPrice"] < lower_limit)
    | (df["TotalPrice"] > upper_limit)
]

print("\n" + "=" * 60)
print("OUTLIER DETECTION")
print("=" * 60)

print("Total Outliers :", len(outliers))

# Top 10 Highest Orders

print("\n" + "=" * 60)
print("TOP 10 HIGHEST VALUE ORDERS")
print("=" * 60)

print(
    df.sort_values(
        by="TotalPrice",
        ascending=False
    ).head(10)
)

# Completion Message

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)