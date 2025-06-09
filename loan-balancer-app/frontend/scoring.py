def calculate_eligibility_score(metrics):
    score = 0
    if metrics["Current Ratio"] >= 1.5:
        score += 1
    if metrics["Debt-to-Equity Ratio"] <= 1.0:
        score += 1
    if metrics["Net Profit Margin"] >= 0.1:
        score += 1
    if metrics["Interest Coverage"] >= 2.0:
        score += 1
    if metrics["Revenue"] >= 100000:
        score += 1

    if score >= 4:
        return "High"
    elif score == 3:
        return "Medium"
    else:
        return "Low"
