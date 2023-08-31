# Financial Ratios as Python Functions

# 1. Gross Margin
def gross_margin(gross_profit, net_sales):
    """
    Concept: Indicates the percentage of revenue available to cover operating and other expenditures.
    Formula: Gross Profit / Net Sales
    
    :param gross_profit: Gross Profit
    :param net_sales: Net Sales
    :return: Gross Margin
    """
    return gross_profit / net_sales

# 2. Operating Margin
def operating_margin(operating_income, net_sales):
    """
    Concept: Measures profitability after subtracting direct costs and operating expenses.
    Formula: Operating Income / Net Sales
    
    :param operating_income: Operating Income
    :param net_sales: Net Sales
    :return: Operating Margin
    """
    return operating_income / net_sales

# 3. Profit Margin
def profit_margin(net_profit, net_sales):
    """
    Concept: Indicates how much of each dollar of revenues is kept as net profit.
    Formula: Net Profit / Net Sales
    
    :param net_profit: Net Profit
    :param net_sales: Net Sales
    :return: Profit Margin
    """
    return net_profit / net_sales

# 4. Return on Equity (ROE)
def roe(net_income, avg_shareholders_equity):
    """
    Concept: Measures a corporation's profitability by revealing net income as a percentage of shareholder's equity.
    Formula: Net Income / Average Shareholders Equity
    
    :param net_income: Net Income
    :param avg_shareholders_equity: Average Shareholders Equity
    :return: ROE
    """
    return net_income / avg_shareholders_equity

# 5. Return on Assets (ROA ratio or Du Pont Ratio)
def roa(net_income, avg_total_assets):
    """
    Concept: Measures how profitable a company is relative to its total assets.
    Formula: Net Income / Average Total Assets
    
    :param net_income: Net Income
    :param avg_total_assets: Average Total Assets
    :return: ROA
    """
    return net_income / avg_total_assets

# 6. Return on Assets (ROA)
def roa_simple(net_income, total_assets):
    """
    Concept: Simplified version of ROA, measures profitability relative to total assets.
    Formula: Net Income / Total Assets
    
    :param net_income: Net Income
    :param total_assets: Total Assets
    :return: Simple ROA
    """
    return net_income / total_assets

# 7. Return on Assets Du Pont (ROA Du Pont)
def roa_dupont(net_income, net_sales, total_assets):
    """
    Concept: Du Pont formula that breaks down ROA into two components for deeper analysis.
    Formula: (Net Income / Net Sales) * (Net Sales / Total Assets)
    
    :param net_income: Net Income
    :param net_sales: Net Sales
    :param total_assets: Total Assets
    :return: ROA Du Pont
    """
    return (net_income / net_sales) * (net_sales / total_assets)

# 8. Return on Equity Du Pont (ROE Du Pont)
def roe_dupont(net_income, net_sales, avg_assets, avg_equity):
    """
    Concept: Du Pont formula for ROE, provides a detailed analysis by breaking it into three components.
    Formula: (Net Income / Net Sales) * (Net Sales / Avg Assets) * (Avg Assets / Avg Equity)
    
    :param net_income: Net Income
    :param net_sales: Net Sales
    :param avg_assets: Average Assets
    :param avg_equity: Average Equity
    :return: ROE Du Pont
    """
    return (net_income / net_sales) * (net_sales / avg_assets) * (avg_assets / avg_equity)

# 9. Return on Net Assets (RONA)
def rona(net_income, fixed_assets, working_capital):
    """
    Concept: Measures how effectively the firm uses its net assets to generate profits.
    Formula: Net Income / (Fixed Assets + Working Capital)
    
    :param net_income: Net Income
    :param fixed_assets: Fixed Assets
    :param working_capital: Working Capital
    :return: RONA
    """
    return net_income / (fixed_assets + working_capital)

# 10. Return on Capital (ROC)
def roc(ebit, tax_rate, invested_capital):
    """
    Concept: Measures the return that an investment generates for capital contributors.
    Formula: EBIT * (1 - Tax Rate) / Invested Capital
    
    :param ebit: Earnings Before Interest and Taxes
    :param tax_rate: Tax Rate
    :param invested_capital: Invested Capital
    :return: ROC
    """
    return ebit * (1 - tax_rate) / invested_capital

# 11. Risk Adjusted Return on Capital (RAROC)
def raroc(expected_return, economic_capital):
    """
    Concept: Measures the return on capital where risk considerations are included.
    Formula: Expected Return / Economic Capital
    
    :param expected_return: Expected Return
    :param economic_capital: Economic Capital
    :return: RAROC
    """
    return expected_return / economic_capital

# 12. Return on Capital Employed (ROCE)
def roce(ebit, capital_employed):
    """
    Concept: Indicates the efficiency and profitability of a company's capital investments.
    Formula: EBIT / Capital Employed
    
    :param ebit: Earnings Before Interest and Taxes
    :param capital_employed: Capital Employed
    :return: ROCE
    """
    return ebit / capital_employed

# 13. Cash Flow Return on Investment (CFROI)
def cfroi(cash_flow, market_recapitalisation):
    """
    Concept: Measures how well a company generates cash flow relative to its market cap.
    Formula: Cash Flow / Market Recapitalisation
    
    :param cash_flow: Cash Flow
    :param market_recapitalisation: Market Recapitalisation
    :return: CFROI
    """
    return cash_flow / market_recapitalisation

# 14. Efficiency Ratio
def efficiency_ratio(non_interest_expense, revenue):
    """
    Concept: Measures a company's ability to generate revenue from its non-interest expenses.
    Formula: Non-Interest expense / Revenue
    
    :param non_interest_expense: Non-Interest Expense
    :param revenue: Revenue
    :return: Efficiency Ratio
    """
    return non_interest_expense / revenue

# 15. Net Gearing
def net_gearing(net_debt, equity):
    """
    Concept: Shows the proportion of company's activities financed by creditors compared to equity.
    Formula: Net Debt / Equity
    
    :param net_debt: Net Debt
    :param equity: Equity
    :return: Net Gearing
    """
    return net_debt / equity

# 16. Basic Earnings Power Ratio
def basic_earnings_power_ratio(ebit, total_assets):
    """
    Concept: Measures a company's basic earning power independently of interest and taxes.
    Formula: EBIT / Total Assets
    
    :param ebit: Earnings Before Interest and Taxes
    :param total_assets: Total Assets
    :return: Basic Earnings Power Ratio
    """
    return ebit / total_assets
