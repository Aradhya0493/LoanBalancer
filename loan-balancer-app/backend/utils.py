def load_financial_data(filepath):
    import pandas as pd
    return pd.read_csv(filepath)

def calculate_current_ratio(current_assets, current_liabilities):
    if current_liabilities == 0:
        return float('inf')
    return current_assets / current_liabilities

def calculate_debt_to_equity(total_debt, total_equity):
    if total_equity == 0:
        return float('inf')
    return total_debt / total_equity

def calculate_net_profit_margin(net_profit, revenue):
    if revenue == 0:
        return 0
    return net_profit / revenue

def calculate_interest_coverage(ebit, interest_expense):
    if interest_expense == 0:
        return float('inf')
    return ebit / interest_expense

def determine_loan_eligibility(current_ratio, debt_to_equity, net_profit_margin, interest_coverage, revenue):
    if current_ratio < 1.5:
        return "Denied", "Current ratio is below threshold."
    if debt_to_equity > 2:
        return "Denied", "Debt-to-equity ratio is too high."
    if net_profit_margin < 0.1:
        return "Denied", "Net profit margin is below threshold."
    if interest_coverage < 1.5:
        return "Denied", "Interest coverage is too low."
    if revenue < 100000:
        return "Denied", "Revenue is below minimum requirement."
    
    return "Approved", "Loan eligibility criteria met."