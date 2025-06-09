def calculate_eligibility_score(metrics):
    # Simple scoring: High if all above thresholds, else Medium or Low
    thresholds = {
        "Current Ratio": 1.5,
        "Debt-to-Equity Ratio": 1.0,
        "Net Profit Margin": 5,
        "Interest Coverage": 2,
        "Revenue": 1000000
    }

    score = "High"
    for key, thresh in thresholds.items():
        val = metrics.get(key, 0)
        if key == "Debt-to-Equity Ratio":
            if val > thresh:
                score = "Low"
                break
        else:
            if val < thresh:
                score = "Low"
                break
    if score == "Low":
        return score

    # If not low, check if near threshold for medium
    for key, thresh in thresholds.items():
        val = metrics.get(key, 0)
        if key == "Debt-to-Equity Ratio":
            if val > thresh * 0.9:
                score = "Medium"
        else:
            if val < thresh * 1.1:
                score = "Medium"
    return score
