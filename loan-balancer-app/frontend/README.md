# Loan Balancer App - Frontend Documentation

## Overview
The Loan Balancer app provides a user-friendly interface for assessing loan eligibility based on various financial metrics. This frontend is built using Gradio, allowing users to input their financial data and receive instant feedback on their loan approval status.

## Setup Instructions

1. **Install Dependencies**:
   Ensure you have Python installed. You can install the required libraries using pip. Run the following command in your terminal:

   ```
   pip install gradio pandas
   ```

2. **Run the Gradio App**:
   To start the Gradio interface, execute the following command in your terminal:

   ```
   python gradio_app.py
   ```

3. **Access the App**:
   Once the app is running, it will provide a local URL (usually `http://localhost:7860`) where you can access the Loan Balancer interface through your web browser.

## Usage

1. **Input Financial Metrics**:
   Enter the required financial metrics such as current ratio, debt-to-equity ratio, net profit margin, interest coverage, and company revenue in the provided fields.

2. **Submit for Evaluation**:
   After entering the data, click the "Evaluate" button to check your loan eligibility.

3. **View Results**:
   The app will display whether the loan is approved or denied, along with the reasons based on the financial metrics provided.

## Features

- User-friendly interface for inputting financial data.
- Instant feedback on loan eligibility.
- Detailed reasons for loan approval or denial based on financial metrics.

## Contributing
If you would like to contribute to the development of this app, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.