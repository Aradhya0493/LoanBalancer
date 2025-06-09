import gradio as gr
import pandas as pd
from utils import (
    check_loan_eligibility,
    plot_metrics,
    autofill_company,
    load_uploaded_csv
)
from scoring import calculate_eligibility_score  # assumed to be correct

# Base data
base_data = pd.read_csv("financial_sheets.csv")
base_data = base_data.rename(columns={"Debt to Equity": "Debt-to-Equity Ratio"})

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🏦 Loan Eligibility Checker with CSV Upload Support")

    company_state = gr.State(value=base_data)

    with gr.Row(equal_height=True):
        with gr.Column():
            gr.Markdown("### 📤 Upload or Select Company")
            file_upload = gr.File(label="Upload CSV", file_types=[".csv"])
            company_dropdown = gr.Dropdown(
                choices=base_data["Company"].tolist(),
                label="Choose a company"
            )

            current_ratio = gr.Number(label="Current Ratio")
            debt_to_equity = gr.Number(label="Debt-to-Equity Ratio")
            net_profit_margin = gr.Number(label="Net Profit Margin")
            interest_coverage = gr.Number(label="Interest Coverage")
            revenue = gr.Number(label="Revenue")
            check_btn = gr.Button("🚀 Check Eligibility")

        with gr.Column():
            status = gr.Textbox(label="Loan Status", interactive=False)
            reason = gr.Textbox(label="Reason", lines=4, interactive=False)
            score_output = gr.Radio(choices=["Low", "Medium", "High"], label="Eligibility Score", interactive=False)

            gr.Markdown("### 📈 Financial Metrics vs Thresholds")
            chart1 = gr.Plot(label="Current Ratio")
            chart2 = gr.Plot(label="Debt-to-Equity Ratio")
            chart3 = gr.Plot(label="Net Profit Margin")
            chart4 = gr.Plot(label="Interest Coverage")
            chart5 = gr.Plot(label="Revenue")

    # --- Functional callbacks ---

    def handle_file_upload(file):
        df = load_uploaded_csv(file)
        if df.empty or "Company" not in df.columns:
            return gr.update(choices=[]), base_data  # fallback
        return gr.update(choices=df["Company"].tolist()), df

    def autofill_from_uploaded(company_name, uploaded_df):
        try:
            row = uploaded_df[uploaded_df["Company"] == company_name]
            if row.empty:
                return 0, 0, 0, 0, 0
            row = row.iloc[0]
            return (
                float(row["Current Ratio"]),
                float(row["Debt-to-Equity Ratio"]),
                float(row["Net Profit Margin"]),
                float(row["Interest Coverage"]),
                float(row["Revenue"])
            )
        except Exception as e:
            print("Autofill error:", e)
            return 0, 0, 0, 0, 0

    def run_all(cr, de, npm, ic, rev):
        status_val, reason_val, metrics = check_loan_eligibility(cr, de, npm, ic, rev)
        figs = plot_metrics(metrics)
        score = calculate_eligibility_score(metrics)
        return status_val, reason_val, score, *figs

    # --- Event wiring ---
    file_upload.change(handle_file_upload, inputs=file_upload, outputs=[company_dropdown, company_state])
    company_dropdown.change(autofill_from_uploaded, inputs=[company_dropdown, company_state],
                            outputs=[current_ratio, debt_to_equity, net_profit_margin, interest_coverage, revenue])
    check_btn.click(run_all,
                    inputs=[current_ratio, debt_to_equity, net_profit_margin, interest_coverage, revenue],
                    outputs=[status, reason, score_output, chart1, chart2, chart3, chart4, chart5])

demo.launch()
