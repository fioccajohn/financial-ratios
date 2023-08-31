# Liquidity Ratios as Python Functions

# 1. Current Ratio (Working Capital Ratio)
def current_ratio(current_assets, current_liabilities):
    """
    Calculate the Current Ratio (Working Capital Ratio).
    
    Concept: Measures the ability of a company to cover its short-term obligations with its short-term assets.
    
    Formula: Current Assets / Current Liabilities
    
    :param current_assets: Total value of all short-term assets
    :param current_liabilities: Total value of all short-term liabilities
    :return: Current Ratio
    """
    return current_assets / current_liabilities

# 2. Acid-test Ratio (Quick Ratio)
def acid_test_ratio(current_assets, inventories, prepayments, current_liabilities):
    """
    Calculate the Acid-Test (Quick) Ratio.
    
    Concept: Measures the ability of a company to use its "quick" assets to immediately extinguish its current liabilities.
    
    Formula: (Current Assets - (Inventories + Prepayments)) / Current Liabilities
    
    :param current_assets: Total value of all short-term assets
    :param inventories: Value of inventories
    :param prepayments: Value of prepayments
    :param current_liabilities: Total value of all short-term liabilities
    :return: Acid-Test Ratio
    """
    return (current_assets - (inventories + prepayments)) / current_liabilities

# 3. Cash Ratio
def cash_ratio(cash_and_marketable_securities, current_liabilities):
    """
    Calculate the Cash Ratio.
    
    Concept: Measures the ability of a company to pay off its current liabilities using only cash and marketable securities.
    
    Formula: Cash and Marketable Securities / Current Liabilities
    
    :param cash_and_marketable_securities: Value of cash and marketable securities
    :param current_liabilities: Total value of all short-term liabilities
    :return: Cash Ratio
    """
    return cash_and_marketable_securities / current_liabilities

# 4. Operating Cash Flow Ratio
def operating_cash_flow_ratio(operating_cash_flow, total_debts):
    """
    Calculate the Operating Cash Flow Ratio.
    
    Concept: Measures how well current liabilities are covered by the cash flow generated from a company's operations.
    
    Formula: Operating Cash Flow / Total Debts
    
    :param operating_cash_flow: Cash flow generated from operations
    :param total_debts: Total value of all debts
    :return: Operating Cash Flow Ratio
    """
    return operating_cash_flow / total_debts

