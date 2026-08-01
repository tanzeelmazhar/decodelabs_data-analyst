"""
E-Commerce Order Data Cleaning Pipeline
---------------------------------------
This script loads the raw e-commerce order dataset,
handles missing values, removes duplicate records,
standardizes the date format, validates pricing,
and exports the cleaned dataset.

Author: Tanzeel Mazhar
"""

import pandas as pd


def clean_data(input_file, output_file):

    print("=" * 50)
    print("E-Commerce Data Cleaning Pipeline Started")
    print("=" * 50)

    # Load dataset
    print(f"\nLoading dataset: {input_file}")
    df = pd.read_excel(input_file)

    print(f"Initial Shape: {df.shape}")

    # 1. Handle Missing Values

    # Replace missing CouponCode values
    df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

    print("✓ Missing CouponCode values filled.")

    # 2. Remove Duplicate Records

    before = len(df)

    df = df.drop_duplicates()

    duplicates_removed = before - len(df)

    print(f"✓ Duplicate Rows Removed: {duplicates_removed}")

    # 3. Standardize Date Format

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

    print("✓ Date format standardized.")

    # 4. Validate Pricing

    df["Expected_Total"] = df["Quantity"] * df["UnitPrice"]

    pricing_errors = df[
        round(df["Expected_Total"], 2)
        != round(df["TotalPrice"], 2)
    ]

    print(f"✓ Pricing Errors Found: {len(pricing_errors)}")

    # Remove helper column
    df.drop(columns=["Expected_Total"], inplace=True)

    # 5. Save Clean Dataset

    df.to_excel(output_file, index=False)

    print(f"\n✅ Cleaned dataset saved as: {output_file}")

    print("=" * 50)
    print("Data Cleaning Completed Successfully!")
    print("=" * 50)


if __name__ == "__main__":

    # Input file (Raw Dataset)
    RAW_DATA = "Dataset for Data Analytics.xlsx"

    # Output file (Cleaned Dataset)
    CLEAN_DATA = "Cleaned_Dataset_task 1.xlsx"

    # Run the cleaning process
    clean_data(RAW_DATA, CLEAN_DATA)