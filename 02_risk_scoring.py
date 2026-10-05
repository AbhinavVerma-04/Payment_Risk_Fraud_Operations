import pandas as pd

df = pd.read_csv("./DATA/transactions.csv")

df["risk_score"] = 0

df.loc[df["ip_risk_score"] >= 70, "risk_score"] += 20

df.loc[df["device_known"] == 0, "risk_score"] += 15

df.loc[df["is_foreign_txn"] == 1, "risk_score"] += 10

print(df["velocity_1h"].describe())
df.loc[df["velocity_1h"] >= 10, "risk_score"] += 20

df.loc[df["amount_vs_avg_ratio"] >= 5, "risk_score"] += 15

df.loc[df["account_age_days"] <= 90, "risk_score"] += 10

df.loc[df["has_2fa"] == 0, "risk_score"] += 5

def classify_risk(score):

    if score >= 60:
        return "High"

    elif score >= 30:
        return "Medium"

    else:
        return "Low"


df["risk_category"] = df["risk_score"].apply(classify_risk)

print(
    pd.crosstab(
        df["risk_category"],
        df["is_fraud"],
        normalize="index"
    ) * 100
)


print("\nRISK SCORE VS FRAUD RATE\n")

risk_fraud_rate = (
    df.groupby("risk_category")["is_fraud"]
    .agg(["count", "sum", "mean"])
)

risk_fraud_rate["fraud_rate_percent"] = (
    risk_fraud_rate["mean"] * 100
)

risk_fraud_rate = risk_fraud_rate.sort_values(
    by="fraud_rate_percent",
    ascending=False
)

print(risk_fraud_rate)

df.to_csv(
    "./DATA/transactions_enriched.csv",
    index=False
)