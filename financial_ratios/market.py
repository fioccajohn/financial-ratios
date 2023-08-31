# Other Market Ratios

# 1. EV/EBITDA
def ev_ebitda(enterprise_value, ebitda):
    """
    Calculate EV/EBITDA Ratio.
    
    Formula: Enterprise Value / EBITDA
    
    :param enterprise_value: Enterprise Value
    :param ebitda: Earnings Before Interest, Taxes, Depreciation, and Amortization
    :return: EV/EBITDA Ratio
    """
    return enterprise_value / ebitda

# 2. EV/Sales
def ev_sales(enterprise_value, net_sales):
    """
    Calculate EV/Sales Ratio.
    
    Formula: Enterprise Value / Net Sales
    
    :param enterprise_value: Enterprise Value
    :param net_sales: Net Sales
    :return: EV/Sales Ratio
    """
    return enterprise_value / net_sales

# 3. Cost/Income Ratio
def cost_income_ratio(cost, income):
    """
    Calculate Cost/Income Ratio.
    
    Formula: Cost / Income
    
    :param cost: Cost
    :param income: Income
    :return: Cost/Income Ratio
    """
    return cost / income
