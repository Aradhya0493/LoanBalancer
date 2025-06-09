from dataclasses import dataclass

@dataclass
class FinancialMetrics:
    current_ratio: float
    debt_to_equity: float
    net_profit_margin: float
    interest_coverage: float
    revenue: float
    return_on_equity: float

class LoanEligibility:
    def __init__(self, metrics: FinancialMetrics):
        self.metrics = metrics

    def is_eligible(self):
        if self.metrics.current_ratio < 1.5:
            return False, "Denied: Current ratio is below the threshold."
        if self.metrics.debt_to_equity > 2.0:
            return False, "Denied: Debt-to-equity ratio is too high."
        if self.metrics.net_profit_margin < 0.1:
            return False, "Denied: Net profit margin is below the threshold."
        if self.metrics.interest_coverage < 1.5:
            return False, "Denied: Interest coverage ratio is too low."
        if self.metrics.revenue < 50000:
            return False, "Denied: Revenue is below the minimum requirement."
        if self.metrics.return_on_equity < 0.15:
            return False, "Denied: Return on equity is below the threshold."
        
        return True, "Approved: All financial metrics meet the eligibility criteria."