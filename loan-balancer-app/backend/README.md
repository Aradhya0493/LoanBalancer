# Loan Balancer App - Backend Documentation

## Overview
The Loan Balancer App is a Flask-based application designed to evaluate loan eligibility based on various financial metrics. This backend component handles the core logic for calculating financial ratios and determining loan approval status.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/loan-balancer-app.git
   cd loan-balancer-app/backend
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## API Endpoints

### Loan Eligibility Check
- **Endpoint:** `/check_eligibility`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "current_ratio": float,
    "debt_to_equity": float,
    "net_profit_margin": float,
    "interest_coverage": float,
    "revenue": float
  }
  ```
- **Response:**
  ```json
  {
    "status": "approved" or "denied",
    "reason": "string"
  }
  ```

## Usage Examples

To check loan eligibility, send a POST request to the `/check_eligibility` endpoint with the required financial metrics in the request body. The response will indicate whether the loan is approved or denied, along with the reason for the decision.

## File Descriptions

- **app.py:** Entry point for the Flask API, sets up routes and handles requests.
- **models.py:** Contains data models and functions for calculating financial metrics.
- **utils.py:** Utility functions for data processing and loan eligibility determination.
- **requirements.txt:** Lists the necessary Python packages for the backend.

## License
This project is licensed under the MIT License - see the LICENSE file for details.