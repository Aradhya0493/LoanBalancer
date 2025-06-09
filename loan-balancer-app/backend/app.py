from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/loan-eligibility', methods=['POST'])
def loan_eligibility():
    data = request.json
    collateral = data.get('collateral')
    debt_to_income_ratio = data.get('debt_to_income_ratio')
    net_profit_margin = data.get('net_profit_margin')
    company_revenue = data.get('company_revenue')
    return_on_equity = data.get('return_on_equity')

    # Example eligibility logic (customize as needed)
    if collateral and debt_to_income_ratio is not None and net_profit_margin is not None and company_revenue is not None and return_on_equity is not None:
        if debt_to_income_ratio < 0.4 and net_profit_margin > 0.1 and company_revenue > 50000 and return_on_equity > 0.15:
            result = {
                "status": "approved",
                "reason": "Eligible based on collateral and financial metrics."
            }
        else:
            reasons = []
            if debt_to_income_ratio >= 0.4:
                reasons.append("Debt-to-income ratio is too high.")
            if net_profit_margin <= 0.1:
                reasons.append("Net profit margin is too low.")
            if company_revenue <= 50000:
                reasons.append("Company revenue is too low.")
            if return_on_equity <= 0.15:
                reasons.append("Return on equity is too low.")
            result = {
                "status": "denied",
                "reason": "Not eligible: " + "; ".join(reasons)
            }
    else:
        result = {
            "status": "denied",
            "reason": "Missing required financial information."
        }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)