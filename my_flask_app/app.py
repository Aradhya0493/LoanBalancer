from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from utils import check_loan_eligibility, plot_metrics, load_uploaded_csv
from scoring import calculate_eligibility_score

app = Flask(__name__)

# Load base data on startup
BASE_DATA_PATH = "financial_sheets.csv"
if not os.path.exists(BASE_DATA_PATH):
    raise FileNotFoundError(f"Missing {BASE_DATA_PATH} file.")

base_data = pd.read_csv(BASE_DATA_PATH)
base_data = base_data.rename(columns={"Debt to Equity": "Debt-to-Equity Ratio"})

# Temp storage for uploaded CSVs
UPLOADED_CSV_PATH = "data/uploaded_temp.csv"
os.makedirs("data", exist_ok=True)

REQUIRED_COLUMNS = [
    "Current Ratio",
    "Debt-to-Equity Ratio",
    "Net Profit Margin",
    "Interest Coverage",
    "Revenue",
    "Company"
]

def clean_uploaded_df(df):
    # Map possible alternate column names to required ones
    rename_map = {
        "Debt to Equity": "Debt-to-Equity Ratio",
        "Net_Profit_Margin": "Net Profit Margin",
        "Debt_to_Equity": "Debt-to-Equity Ratio",
        "Interest_Coverage": "Interest Coverage",
        "Current_Ratio": "Current Ratio",
        "Revenue": "Revenue",
        "Company": "Company"
    }
    df = df.rename(columns=rename_map)
    # Only keep required columns
    return df[[col for col in REQUIRED_COLUMNS if col in df.columns]]


@app.route("/")
def home():
    # Send base company list for dropdown on page load
    companies = base_data["Company"].dropna().tolist()
    return render_template("index.html", companies=companies)


@app.route("/api/upload_csv", methods=["POST"])
def upload_csv():
    try:
        file = request.files.get("file")
        if not file:
            return jsonify({"error": "No file uploaded."}), 400

        df_uploaded = pd.read_csv(file)
        df_uploaded = clean_uploaded_df(df_uploaded)

        if "Company" not in df_uploaded.columns:
            return jsonify({"error": "CSV must contain 'Company' column."}), 400

        # Save to temp file for session (simple approach)
        df_uploaded.to_csv(UPLOADED_CSV_PATH, index=False)

        companies = df_uploaded["Company"].dropna().tolist()
        return jsonify({"companies": companies})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/get_company_data", methods=["POST"])
def get_company_data():
    try:
        data = request.json
        company_name = data.get("company")
        if not company_name:
            return jsonify({"error": "Company name not provided."}), 400

        # Try uploaded data first, fallback to base data
        if os.path.exists(UPLOADED_CSV_PATH):
            df = pd.read_csv(UPLOADED_CSV_PATH)
        else:
            df = base_data

        df = clean_uploaded_df(df)

        row = df[df["Company"] == company_name]
        if row.empty:
            return jsonify({"error": "Company not found."}), 404

        row = row.iloc[0]
        return jsonify({
            "Current Ratio": float(row.get("Current Ratio", 0)),
            "Debt-to-Equity Ratio": float(row.get("Debt-to-Equity Ratio", 0)),
            "Net Profit Margin": float(row.get("Net Profit Margin", 0)),
            "Interest Coverage": float(row.get("Interest Coverage", 0)),
            "Revenue": float(row.get("Revenue", 0))
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/predict_loan_approval", methods=["POST"])
def predict_loan_approval():
    try:
        data = request.json
        cr = float(data.get("Current Ratio", 0))
        de = float(data.get("Debt-to-Equity Ratio", 0))
        npm = float(data.get("Net Profit Margin", 0))
        ic = float(data.get("Interest Coverage", 0))
        rev = float(data.get("Revenue", 0))

        status_val, reason_val, metrics = check_loan_eligibility(cr, de, npm, ic, rev)
        figs = plot_metrics(metrics)
        score = calculate_eligibility_score(metrics)

        return jsonify({
            "status": status_val,
            "reason": reason_val,
            "score": score,
            "metrics": metrics
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/dashboard_metrics")
def dashboard_metrics():
    # Use uploaded CSV if available, else base data
    if os.path.exists(UPLOADED_CSV_PATH):
        df = pd.read_csv(UPLOADED_CSV_PATH)
    else:
        df = base_data

    # Ensure columns are named correctly
    df = df.rename(columns={"Debt to Equity": "Debt-to-Equity Ratio"})

    # Compute averages, handling missing columns gracefully
    avg_current_ratio = df["Current Ratio"].mean() if "Current Ratio" in df else 0
    avg_debt_to_equity = df["Debt-to-Equity Ratio"].mean() if "Debt-to-Equity Ratio" in df else 0
    avg_net_profit_margin = df["Net Profit Margin"].mean() if "Net Profit Margin" in df else 0

    return jsonify({
        "avgCurrentRatio": round(avg_current_ratio, 2),
        "avgDebtToEquity": round(avg_debt_to_equity, 2),
        "avgNetProfitMargin": round(avg_net_profit_margin, 2)
    })

@app.route("/dashboard")
def dashboard():
    # Placeholder dashboard page
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
