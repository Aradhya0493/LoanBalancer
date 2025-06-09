import matplotlib.pyplot as plt
import pandas as pd

# Define thresholds
thresholds = {
    "Current Ratio": 1.5,
    "Debt-to-Equity Ratio": 1.0,
    "Net Profit Margin": 0.1,
    "Interest Coverage": 2.0,
    "Revenue": 100000
}

# Base dataset
data = pd.read_csv("financial_sheets.csv")
data = data.rename(columns={"Debt to Equity": "Debt-to-Equity Ratio"})

def check_loan_eligibility(current_ratio, debt_to_equity, net_profit_margin, interest_coverage, revenue):
    metrics = {
        "Current Ratio": current_ratio,
        "Debt-to-Equity Ratio": debt_to_equity,
        "Net Profit Margin": net_profit_margin,
        "Interest Coverage": interest_coverage,
        "Revenue": revenue
    }

    reasons = []
    for metric, value in metrics.items():
        if metric == "Debt-to-Equity Ratio":
            if value > thresholds[metric]:
                reasons.append(f"{metric} is above the threshold.")
        else:
            if value < thresholds[metric]:
                reasons.append(f"{metric} is below the threshold.")

    status = "✅ Loan Approved" if not reasons else "❌ Loan Denied"
    return status, ", ".join(reasons), metrics

def plot_metrics(metrics):
    figs = []
    for key, value in metrics.items():
        fig, ax = plt.subplots(figsize=(3, 2))
        ax.barh(["Company Value"], [value], color='skyblue')
        ax.axvline(thresholds[key], color='red', linestyle='--', label='Threshold')
        ax.set_title(f"{key}")
        ax.set_xlabel("Value")
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.3)
        plt.tight_layout()
        figs.append(fig)
    return figs

def autofill_company(company_name):
    row = data[data["Company"] == company_name].iloc[0]
    return (
        float(row["Current Ratio"]),
        float(row["Debt-to-Equity Ratio"]),
        float(row["Net Profit Margin"]),
        float(row["Interest Coverage"]),
        float(row["Revenue"])
    )

def load_uploaded_csv(file_obj):
    try:
        # uploaded_data = pd.read_csv(file_obj.name)
        uploaded_data = pd.read_csv(file_obj)

        uploaded_data = uploaded_data.rename(columns={
            "Debt to Equity": "Debt-to-Equity Ratio",
            "Current Ratio": "Current Ratio",
            "Net Profit Margin": "Net Profit Margin",
            "Interest Coverage": "Interest Coverage",
            "Revenue": "Revenue",
            "Company": "Company"
        })

        # Clean and cast types
        metric_cols = ["Current Ratio", "Debt-to-Equity Ratio", "Net Profit Margin", "Interest Coverage", "Revenue"]
        for col in metric_cols:
            uploaded_data[col] = pd.to_numeric(uploaded_data[col], errors="coerce").fillna(0)

        return uploaded_data
    except Exception as e:
        print("CSV parsing failed:", e)
        return pd.DataFrame()
