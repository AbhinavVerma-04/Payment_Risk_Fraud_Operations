import pandas as pd

transactions = pd.read_csv("./DATA/transactions.csv")

print(transactions.head())
print(transactions.shape)
print(transactions.columns)

print(transactions.info())

print(transactions.isnull().sum())

print(transactions.dtypes)

print(transactions["is_fraud"].value_counts())

print(transactions["is_fraud"].value_counts(normalize=True) * 100)


print("\n\nCategory Wise Analysis!!\n\n")

fraud_transactions = transactions[
    transactions["is_fraud"] == 1
]

print(fraud_transactions["fraud_pattern"].value_counts())

print(
    fraud_transactions["fraud_pattern"]
    .value_counts(normalize=True) * 100
)

## PATTERN SUMMARY

fraud_summary = (
    fraud_transactions
    .groupby("fraud_pattern")
    .agg(
        transactions=("transaction_id", "count"),
        total_amount=("amount", "sum"),
        average_amount=("amount", "mean")
    )
    .sort_values("transactions", ascending=False)
)

print("\n",fraud_summary,"\n")

print(transactions["amount"].describe())

print(
    transactions.groupby("is_fraud")["amount"]
    .agg(["count", "mean", "median", "max"])
)


## HOURLY FRAUD

print("\nHOURLY FRAUD!!\n")

hourly_fraud = (
    transactions
    .groupby("hour_of_day")
    .agg(
        total_transactions=("transaction_id", "count"),
        fraud_transactions=("is_fraud", "sum")
    )
)

hourly_fraud["fraud_rate"] = (
    hourly_fraud["fraud_transactions"] /
    hourly_fraud["total_transactions"] * 100
)

print(hourly_fraud)


print("\n")

