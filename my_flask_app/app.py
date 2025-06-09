from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Make sure the charts folder exists
os.makedirs('static/charts', exist_ok=True)

def check_loan_eligibility(current_ratio, debt_to_equity, net_profit_margin, interest_coverage, revenue):
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

def generate_dashboard_chart():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    approved = [12, 15, 18, 14, 20, 16]
    rejected = [6, 5, 5, 4, 3, 7]

    plt.figure(figsize=(8, 4))
    plt.bar(months, approved, color='green', label='Approved')
    plt.bar(months, rejected, bottom=approved, color='red', label='Rejected')
    plt.title("Monthly Approval Trends")
    plt.legend()
    plt.tight_layout()

    chart_path = 'static/charts/loan_approval_trends.png'
    plt.savefig(chart_path)
    plt.close()
    return chart_path

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    reasons = None
    if request.method == 'POST':
        # Get form data and convert to floats
        try:
            current_ratio = float(request.form['current_ratio'])
            debt_to_equity = float(request.form['debt_to_equity'])
            net_profit_margin = float(request.form['net_profit_margin'])
            interest_coverage = float(request.form['interest_coverage'])
            revenue = float(request.form['revenue'])
            
            result, reasons = check_loan_eligibility(current_ratio, debt_to_equity, net_profit_margin, interest_coverage, revenue)
        except ValueError:
            result = "Invalid input"
            reasons = "Please enter valid numerical values."

    chart_url = url_for('static', filename='charts/loan_approval_trends.png')

    return render_template('index.html', 
                           result=result, reasons=reasons, chart_url=chart_url)

@app.route('/generate-chart')
def generate_chart():
    chart_path = generate_dashboard_chart()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)