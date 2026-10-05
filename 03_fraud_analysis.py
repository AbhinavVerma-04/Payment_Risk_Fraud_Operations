import pandas as pd

accounts = pd.read_csv(
    "./DATA/account_profiles.csv"
)

print(accounts.head())
print(accounts.info())

high_risk_accounts = accounts[
    accounts["is_high_risk"] == 1
]

print(high_risk_accounts.shape)

high_risk_accounts = high_risk_accounts.sort_values(
    "risk_score",
    ascending=False
)

top_100 = high_risk_accounts.head(100)

print(top_100)

patterns = pd.read_csv(
    "./DATA/fraud_patterns.csv"
)

print(patterns)

network = pd.read_csv(
    "./DATA/network_edges.csv"
)

print(network.head())
print(network.info())

from collections import Counter

connections = Counter(
    network["account_a"].tolist()
    +
    network["account_b"].tolist()
)

print(connections.most_common(20))

df=pd.read_csv("./DATA/transactions.csv")

high_ip_risk_pct = (
    (df["ip_risk_score"] >= 70).sum()
    / len(df)
    * 100
)

print("High IP Risk %:", round(high_ip_risk_pct, 2))

unknown_device_pct = (
    (df["device_known"] == 0).sum()
    / len(df)
    * 100
)

print("Unknown Device %:", round(unknown_device_pct, 2))

high_velocity_pct = (
    (df["velocity_1h"] >= 5).sum()
    / len(df)
    * 100
)

print("High Velocity %:", round(high_velocity_pct, 2))

foreign_txn_pct = (
    (df["is_foreign_txn"] == 1).sum()
    / len(df)
    * 100
)

print("Foreign Transaction %:", round(foreign_txn_pct, 2))

high_amount_anomaly_pct = (
    (df["amount_vs_avg_ratio"] >= 3).sum()
    / len(df)
    * 100
)

print(
    "High Amount Anomaly %:",
    round(high_amount_anomaly_pct, 2)
)