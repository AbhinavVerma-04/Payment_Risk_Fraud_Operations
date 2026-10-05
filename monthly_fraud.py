import pandas as pd

# Load data
df = pd.read_csv("./DATA/transactions.csv")

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Create month column
df["month"] = df["timestamp"].dt.to_period("M").astype(str)

# Monthly summary
monthly = (
    df.groupby("month")
    .agg(
        total_transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum"),
        total_amount=("amount", "sum")
    )
    .reset_index()
)

# Fraud rate
monthly["fraud_rate"] = (
    monthly["fraud_transactions"]
    / monthly["total_transactions"]
    * 100
)

# Fraud amount
fraud_amount = (
    df[df["is_fraud"] == 1]
    .groupby("month")["amount"]
    .sum()
    .reset_index(name="fraud_amount")
)

# Merge
monthly = monthly.merge(
    fraud_amount,
    on="month",
    how="left"
)

# Fill months with no fraud
monthly["fraud_amount"] = monthly["fraud_amount"].fillna(0)

# Round
monthly["fraud_rate"] = monthly["fraud_rate"].round(2)
monthly["total_amount"] = monthly["total_amount"].round(2)
monthly["fraud_amount"] = monthly["fraud_amount"].round(2)

# Save
monthly.to_csv("./DATA/monthly_fraud_trend.csv", index=False)

print(monthly)
print("\nFile created: monthly_fraud_trend.csv")