# Loan Balancer App

The Loan Balancer App is a financial application designed to assess loan eligibility based on various financial metrics. It utilizes a Flask backend to handle API requests and a Gradio frontend for user interaction.

## Project Structure

```
loan-balancer-app
├── backend
│   ├── app.py               # Entry point for the Flask API
│   ├── models.py            # Data models and calculations for loan eligibility
│   ├── utils.py             # Utility functions for data processing
│   ├── requirements.txt      # Python dependencies for the backend
│   └── README.md            # Documentation for the backend
├── frontend
│   ├── gradio_app.py        # Gradio interface for user interaction
│   └── README.md            # Documentation for the frontend
├── data
│   └── financial_sheets.csv  # Financial data for calculations
├── .gitignore               # Files and directories to ignore in Git
└── README.md                # Overview of the entire project
```

## Features

- **Loan Eligibility Assessment**: The app evaluates loan eligibility based on:
  - Current Ratio
  - Debt-to-Equity Ratio
  - Net Profit Margin
  - Interest Coverage Ratio
  - Revenue Score

- **Decision Output**: The app provides a clear output indicating whether the loan is approved or denied, along with the reasons based on the financial metrics.

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask API:
   ```
   python app.py
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Run the Gradio app:
   ```
   python gradio_app.py
   ```

## Usage

- Access the Gradio interface in your web browser to input financial metrics and receive loan eligibility results.
- The backend API can also be accessed directly for programmatic checks.

## Data Source

The financial data used for calculations is sourced from the Kaggle dataset available at [Kaggle Financial Sheets Dataset](https://www.kaggle.com/datasets/pacificrm/financial-sheets).

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.