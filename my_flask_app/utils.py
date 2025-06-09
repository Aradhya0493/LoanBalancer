import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from dataclasses import dataclass

@dataclass
class FinancialMetrics:
    current_ratio: float
    debt_to_equity: float
    net_profit_margin: float
    interest_coverage: float
    revenue: float

class LoanEligibility:
    def __init__(self, metrics: FinancialMetrics):
        self.metrics = metrics

    def is_eligible(self):
        if self.metrics.current_ratio < 1.5:
            return False, "Denied: Current ratio is below the threshold."
        if self.metrics.debt_to_equity > 2.0:
            return False, "Denied: Debt-to-equity ratio is too high."
        if self.metrics.net_profit_margin < 0.1:
            return False, "Denied: Net profit margin is below the threshold."
        if self.metrics.interest_coverage < 1.5:
            return False, "Denied: Interest coverage ratio is too low."
        if self.metrics.revenue < 50000:
            return False, "Denied: Revenue is below the minimum requirement."
        
        return True, "Approved: All financial metrics meet the eligibility criteria."

def load_uploaded_csv(file):
    try:
        df = pd.read_csv(file)
        df = df.rename(columns={"Debt to Equity": "Debt-to-Equity Ratio"})
        return df
    except Exception:
        return pd.DataFrame()

def check_loan_eligibility(current_ratio, debt_to_equity, net_profit_margin, interest_coverage, revenue):
    metrics = FinancialMetrics(
        current_ratio=current_ratio,
        debt_to_equity=debt_to_equity,
        net_profit_margin=net_profit_margin,
        interest_coverage=interest_coverage,
        revenue=revenue
    )
    eligibility = LoanEligibility(metrics)
    eligible, reason = eligibility.is_eligible()
    status = "Eligible" if eligible else "Not Eligible"
    metrics_dict = {
        "Current Ratio": current_ratio,
        "Debt-to-Equity Ratio": debt_to_equity,
        "Net Profit Margin": net_profit_margin,
        "Interest Coverage": interest_coverage,
        "Revenue": revenue
    }
    return status, reason, metrics_dict


def plot_metrics(metrics):
    # Return simple dict for charts (x and y for bar chart)
    labels = list(metrics.keys())
    values = [metrics[k] for k in labels]
    thresholds = {
        "Current Ratio": 1.5,
        "Debt-to-Equity Ratio": 1.0,
        "Net Profit Margin": 5,
        "Interest Coverage": 2,
        "Revenue": 1000000
    }

    charts_data = []
    for label in labels:
        val = metrics[label]
        thresh = thresholds[label]

        chart = {
            "label": label,
            "value": val,
            "threshold": thresh
        }
        charts_data.append(chart)
    return charts_data
