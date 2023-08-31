# Activity Ratios as Python Functions

# 1. Average Collection Period
def average_collection_period(accounts_receivable, annual_credit_sales):
    """
    Calculate the Average Collection Period.
    
    Concept: Measures the average number of days it takes to collect accounts receivable.
    
    Formula: (Accounts Receivable / Annual Credit Sales) x 365 Days
    
    :param accounts_receivable: Value of accounts receivable
    :param annual_credit_sales: Annual credit sales
    :return: Average Collection Period in days
    """
    return (accounts_receivable / annual_credit_sales) * 365

# 2. Degree of Operating Leverage (DOL)
def degree_of_operating_leverage(delta_net_operating_income, delta_sales):
    """
    Calculate the Degree of Operating Leverage (DOL).
    
    Concept: Measures the sensitivity of net operating income to changes in sales.
    
    Formula: Percent Change in Net Operating Income / Percent Change in Sales
    
    :param delta_net_operating_income: Percent change in net operating income
    :param delta_sales: Percent change in sales
    :return: Degree of Operating Leverage
    """
    return delta_net_operating_income / delta_sales

# 3. DSO Ratio
def dso_ratio(accounts_receivable, total_annual_sales):
    """
    Calculate the DSO Ratio.
    
    Concept: Measures how many days it takes, on average, to collect revenue after a sale has been made.
    
    Formula: (Accounts Receivable / Total Annual Sales) x 365 Days
    
    :param accounts_receivable: Value of accounts receivable
    :param total_annual_sales: Total annual sales
    :return: DSO Ratio in days
    """
    return (accounts_receivable / total_annual_sales) * 365

# 4. Average Payment Period
def average_payment_period(accounts_payable, annual_credit_purchases):
    """
    Calculate the Average Payment Period.
    
    Concept: Measures the average time a company takes to pay its suppliers.
    
    Formula: (Accounts Payable / Annual Credit Purchases) x 365 Days
    
    :param accounts_payable: Value of accounts payable
    :param annual_credit_purchases: Annual credit purchases
    :return: Average Payment Period in days
    """
    return (accounts_payable / annual_credit_purchases) * 365

# 5. Asset Turnover
def asset_turnover(net_sales, total_assets):
    """
    Calculate the Asset Turnover Ratio.
    
    Concept: Measures the efficiency of a company's assets to generate sales or revenue.
    
    Formula: Net Sales / Total Assets
    
    :param net_sales: Net sales
    :param total_assets: Total assets
    :return: Asset Turnover Ratio
    """
    return net_sales / total_assets

# 6. Stock Turnover Ratio
def stock_turnover_ratio(cost_of_goods_sold, avg_inventory):
    """
    Calculate the Stock Turnover Ratio.
    
    Concept: Measures how many times a company's inventory is sold and replaced over a period.
    
    Formula: Cost of Goods Sold / Average Inventory
    
    :param cost_of_goods_sold: Cost of goods sold
    :param avg_inventory: Average inventory
    :return: Stock Turnover Ratio
    """
    return cost_of_goods_sold / avg_inventory

# 7. Receivables Turnover Ratio
def receivables_turnover_ratio(net_credit_sales, avg_net_receivables):
    """
    Calculate the Receivables Turnover Ratio.
    
    Concept: Measures how efficiently a company uses its assets.
    
    Formula: Net Credit Sales / Average Net Receivables
    
    :param net_credit_sales: Net credit sales
    :param avg_net_receivables: Average net receivables
    :return: Receivables Turnover Ratio
    """
    return net_credit_sales / avg_net_receivables

# 8. Inventory Conversion Ratio
def inventory_conversion_ratio(inventory_turnover):
    """
    Calculate the Inventory Conversion Ratio.
    
    Concept: Measures the number of days it takes to sell the inventory.
    
    Formula: 365 Days / Inventory Turnover
    
    :param inventory_turnover: Inventory Turnover Ratio
    :return: Inventory Conversion Ratio in days
    """
    return 365 / inventory_turnover

# 9. Inventory Conversion Period
def inventory_conversion_period(inventory, cost_of_goods_sold):
    """
    Calculate the Inventory Conversion Period.
    
    Concept: Measures how long a company takes to sell its inventory.
    
    Formula: (Inventory / Cost of Goods Sold) x 365 Days
    
    :param inventory: Value of inventory
    :param cost_of_goods_sold: Cost of goods sold
    :return: Inventory Conversion Period in days
    """
    return (inventory / cost_of_goods_sold) * 365

# Activity Ratios related to Conversion Periods and Cash Conversion Cycle

# 10. Receivables Conversion Period
def receivables_conversion_period(receivables, net_sales):
    """
    Calculate the Receivables Conversion Period.
    
    Concept: Measures how many days it takes, on average, to collect the accounts receivable.
    
    Formula: (Receivables / Net Sales) * 365 Days
    
    :param receivables: Amount of receivables
    :param net_sales: Net sales
    :return: Receivables Conversion Period in Days
    """
    return (receivables / net_sales) * 365

# 11. Payables Conversion Period
def payables_conversion_period(accounts_payables, purchases):
    """
    Calculate the Payables Conversion Period.
    
    Concept: Measures how many days it takes, on average, to pay off its accounts payable.
    
    Formula: (Accounts Payables / Purchases) * 365 Days
    
    :param accounts_payables: Amount of accounts payables
    :param purchases: Amount of purchases
    :return: Payables Conversion Period in Days
    """
    return (accounts_payables / purchases) * 365

# 12. Cash Conversion Cycle
def cash_conversion_cycle(inventory_conversion_period, receivables_conversion_period, payables_conversion_period):
    """
    Calculate the Cash Conversion Cycle.
    
    Concept: Measures the time it takes for a company to convert resource inputs into cash.
    
    Formula: Inventory Conversion Period + Receivables Conversion Period - Payables Conversion Period
    
    :param inventory_conversion_period: Inventory conversion period in days
    :param receivables_conversion_period: Receivables conversion period in days
    :param payables_conversion_period: Payables conversion period in days
    :return: Cash Conversion Cycle in Days
    """
    return inventory_conversion_period + receivables_conversion_period - payables_conversion_period
