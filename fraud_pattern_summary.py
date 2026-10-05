import pandas as pd

# ============================================================
# 1. LOAD TRANSACTION DATA
# ============================================================

file_path = "./DATA/transactions.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Total rows:", len(df))


# ============================================================
# 2. KEEP ONLY FRAUD TRANSACTIONS
# ============================================================

fraud_df = df[df["is_fraud"] == 1].copy()

print("Total fraud transactions:", len(fraud_df))


# ============================================================
# 3. FRAUD PATTERN ANALYSIS
# ============================================================

fraud_pattern_summary = (
    fraud_df
    .groupby("fraud_pattern")
    .agg(
        transactions=("transaction_id", "count"),
        total_fraud_amount=("amount", "sum"),
        average_fraud_amount=("amount", "mean"),
        median_fraud_amount=("amount", "median"),
        minimum_fraud_amount=("amount", "min"),
        maximum_fraud_amount=("amount", "max")
    )
    .reset_index()
)


# ============================================================
# 4. CALCULATE % OF TOTAL FRAUD
# ============================================================

total_fraud_transactions = len(fraud_df)

fraud_pattern_summary["fraud_share_percent"] = (
    fraud_pattern_summary["transactions"]
    / total_fraud_transactions
    * 100
)


# ============================================================
# 5. ROUND VALUES FOR EXCEL
# ============================================================

fraud_pattern_summary["fraud_share_percent"] = (
    fraud_pattern_summary["fraud_share_percent"].round(2)
)

fraud_pattern_summary["total_fraud_amount"] = (
    fraud_pattern_summary["total_fraud_amount"].round(2)
)

fraud_pattern_summary["average_fraud_amount"] = (
    fraud_pattern_summary["average_fraud_amount"].round(2)
)

fraud_pattern_summary["median_fraud_amount"] = (
    fraud_pattern_summary["median_fraud_amount"].round(2)
)

fraud_pattern_summary["minimum_fraud_amount"] = (
    fraud_pattern_summary["minimum_fraud_amount"].round(2)
)

fraud_pattern_summary["maximum_fraud_amount"] = (
    fraud_pattern_summary["maximum_fraud_amount"].round(2)
)


# ============================================================
# 6. SORT BY NUMBER OF FRAUD TRANSACTIONS
# ============================================================

fraud_pattern_summary = fraud_pattern_summary.sort_values(
    by="transactions",
    ascending=False
)


# ============================================================
# 7. RENAME COLUMNS FOR EXCEL
# ============================================================

fraud_pattern_summary = fraud_pattern_summary.rename(
    columns={
        "fraud_pattern": "Fraud Pattern",
        "transactions": "Fraud Transactions",
        "fraud_share_percent": "% of Total Fraud",
        "total_fraud_amount": "Total Fraud Amount",
        "average_fraud_amount": "Average Fraud Amount",
        "median_fraud_amount": "Median Fraud Amount",
        "minimum_fraud_amount": "Minimum Fraud Amount",
        "maximum_fraud_amount": "Maximum Fraud Amount"
    }
)


# ============================================================
# 8. DISPLAY RESULT
# ============================================================

print("\n==========================================")
print("FRAUD PATTERN SUMMARY")
print("==========================================")

print(fraud_pattern_summary.to_string(index=False))


# ============================================================
# 9. OVERALL FRAUD METRICS
# ============================================================

total_transactions = len(df)
total_fraud = len(fraud_df)
total_fraud_amount = fraud_df["amount"].sum()

overall_fraud_rate = (
    total_fraud / total_transactions * 100
)

overall_average_fraud_amount = (
    fraud_df["amount"].mean()
)


print("\n==========================================")
print("OVERALL FRAUD METRICS")
print("==========================================")

print("Total Transactions:", total_transactions)
print("Total Fraud Transactions:", total_fraud)
print("Overall Fraud Rate:", round(overall_fraud_rate, 2), "%")
print("Total Fraud Amount:", round(total_fraud_amount, 2))
print(
    "Average Fraud Transaction Amount:",
    round(overall_average_fraud_amount, 2)
)



# ============================================================
# 10. SAVE FOR EXCEL
# ============================================================

output_file = "./DATA/fraud_pattern_summary.csv"

fraud_pattern_summary.to_csv(
    output_file,
    index=False
)

print("\nFile created successfully:", output_file)

