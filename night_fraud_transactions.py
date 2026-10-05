import pandas as pd

# Load data
df = pd.read_csv("./DATA/transactions.csv")



df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour

night_fraud = df[
    (df["hour"].between(0, 4)) &
    (df["is_fraud"] == 1)
].shape[0]

morning_fraud = df[
    (df["hour"].between(5, 11)) &
    (df["is_fraud"] == 1)
].shape[0]

print("Night Fraud Transactions:", night_fraud)
print("Morning Fraud Transactions:", morning_fraud)

ratio = night_fraud / morning_fraud

print("Night : Morning Fraud Ratio:",
      round(ratio, 2), ": 1")