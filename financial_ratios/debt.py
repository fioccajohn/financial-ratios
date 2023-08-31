# Debt Ratios as Python Functions

# 1. Debt Ratio
def debt_ratio(total_liabilities, total_assets):
    """
    Calculate the Debt Ratio.
    
    Concept: Measures the proportion of a company's assets financed by debt.
    
    Formula: Total Liabilities / Total Assets
    
    :param total_liabilities: Total liabilities
    :param total_assets: Total assets
    :return: Debt Ratio
    """
    return total_liabilities / total_assets

# 2. Debt to Equity Ratio
def debt_to_equity(long_term_debt, value_of_leases, avg_shareholders_equity):
    """
    Calculate the Debt to Equity Ratio.
    
    Concept: Measures a company's financial leverage.
    
    Formula: (Long-term Debt + Value of Leases) / Average Shareholders Equity
    
    :param long_term_debt: Long-term debt
    :param value_of_leases: Value of leases
    :param avg_shareholders_equity: Average shareholders equity
    :return: Debt to Equity Ratio
    """
    return (long_term_debt + value_of_leases) / avg_shareholders_equity

# 3. Long-term Debt to Equity
def long_term_debt_to_equity(long_term_debt, avg_shareholders_equity):
    """
    Calculate the Long-term Debt to Equity Ratio.
    
    Concept: Measures the proportion of long-term debt relative to equity capital.
    
    Formula: Long-term Debt / Average Shareholders Equity
    
    :param long_term_debt: Long-term debt
    :param avg_shareholders_equity: Average shareholders equity
    :return: Long-term Debt to Equity Ratio
    """
    return long_term_debt / avg_shareholders_equity

# 4. Times Interest Earned Ratio (Interest Coverage Ratio)
def times_interest_earned(ebit, annual_interest_expense, net_income=None):
    """
    Calculate the Times Interest Earned Ratio or Interest Coverage Ratio.
    
    Concept: Measures the company's ability to pay its interest expenses.
    
    Formula Option 1: EBIT / Annual Interest Expense
    Formula Option 2: Net Income / Annual Interest Expense (Use if EBIT not available)
    
    :param ebit: Earnings before interest and taxes
    :param annual_interest_expense: Annual interest expense
    :param net_income: Net income (Optional, use if EBIT not available)
    :return: Times Interest Earned Ratio
    """
    if ebit is not None:
        return ebit / annual_interest_expense
    elif net_income is not None:
        return net_income / annual_interest_expense
    else:
        return "Either EBIT or Net Income must be provided."

# 5. Debt Service Coverage Ratio
def debt_service_coverage_ratio(net_operating_income, total_debt_service):
    """
    Calculate the Debt Service Coverage Ratio.
    
    Concept: Measures the cash flow available to pay current debt obligations.
    
    Formula: Net Operating Income / Total Debt Service
    
    :param net_operating_income: Net operating income
    :param total_debt_service: Total debt service
    :return: Debt Service Coverage Ratio
    """
    return net_operating_income / total_debt_service
