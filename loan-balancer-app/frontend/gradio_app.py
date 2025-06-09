import gradio as gr
import pandas as pd

# Load financial data
data = pd.read_csv('../data/financial_sheets.csv')

def check_loan_eligibility(current_ratio, debt_to_equity, net_profit_margin, interest_coverage, revenue):
    # Define thresholds for eligibility
    thresholds = {
        "current_ratio": 1.5,
        "debt_to_equity": 1.0,
        "net_profit_margin": 0.1,
        "interest_coverage": 2.0,
        "revenue": 100000
    }
    
    reasons = []
    
    if current_ratio < thresholds["current_ratio"]:
        reasons.append("Current ratio is below the threshold.")
    if debt_to_equity > thresholds["debt_to_equity"]:
        reasons.append("Debt-to-equity ratio is above the threshold.")
    if net_profit_margin < thresholds["net_profit_margin"]:
        reasons.append("Net profit margin is below the threshold.")
    if interest_coverage < thresholds["interest_coverage"]:
        reasons.append("Interest coverage is below the threshold.")
    if revenue < thresholds["revenue"]:
        reasons.append("Revenue is below the threshold.")
    
    if reasons:
        return "Loan Denied", ", ".join(reasons)
    else:
        return "Loan Approved", "All criteria met."

# Gradio interface
iface = gr.Interface(
    fn=check_loan_eligibility,
    inputs=[
        gr.Number(label="Current Ratio"),
        gr.Number(label="Debt-to-Equity Ratio"),
        gr.Number(label="Net Profit Margin"),
        gr.Number(label="Interest Coverage"),
        gr.Number(label="Revenue")
    ],
    outputs=[
        gr.Textbox(label="Loan Status"),
        gr.Textbox(label="Reason")
    ],
    title="Loan Eligibility Checker",
    description="Enter financial metrics to check loan eligibility."
)

if __name__ == "__main__":
    iface.launch()