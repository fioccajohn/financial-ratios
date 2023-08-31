# Sector-specific Ratios

# 1. EV/capacity
def ev_capacity(enterprise_value, capacity):
    """
    Calculate EV/Capacity Ratio (Sector-Specific).
    
    Formula: Enterprise Value / Capacity
    
    :param enterprise_value: Enterprise Value
    :param capacity: Capacity
    :return: EV/Capacity Ratio
    """
    return enterprise_value / capacity

# 2. EV/output
def ev_output(enterprise_value, output):
    """
    Calculate EV/Output Ratio (Sector-Specific).
    
    Formula: Enterprise Value / Output
    
    :param enterprise_value: Enterprise Value
    :param output: Output
    :return: EV/Output Ratio
    """
    return enterprise_value / output
