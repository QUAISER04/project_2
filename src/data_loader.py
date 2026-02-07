import pandas as pd
import numpy as np

def load_data(filepath):
    """
    Loads data from the Excel file.
    Args:
        filepath (str): Path to the Excel file.
    Returns:
        dict: A dictionary of DataFrames for each sheet.
    """
    try:
        sheets = pd.read_excel(filepath, sheet_name=None)
        return sheets
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(sheets):
    """
    Cleans and preprocesses the data.
    Args:
        sheets (dict): Dictionary of DataFrames loaded from Excel.
    Returns:
        pd.DataFrame: Merged and cleaned main sales DataFrame.
    """
    # Extract sheets
    df_sales = sheets['Sales Orders']
    df_customers = sheets['Customers']
    df_products = sheets['Products']
    df_regions = sheets['Regions']
    
    # 1. Merge Data
    # Merge Sales with Customers
    # Sales has 'Customer Name Index', Customers has 'Customer Index'
    df_merged = pd.merge(df_sales, df_customers, left_on='Customer Name Index', right_on='Customer Index', how='left')
    
    # Merge with Products
    # Products sheet has 'Index' and 'Product Name'
    df_merged = pd.merge(df_merged, df_products, left_on='Product Description Index', right_on='Index', how='left')
    
    # Merge with Regions
    # Regions usually has 'Index' too? Let's assume 'Index' based on pattern or 'Delivery Region Index' match.
    # Previous code assumed 'Delivery Region Index' mapping.
    # If df_regions has 'Index', we map 'Delivery Region Index' -> 'Index'
    # Let's inspect quietly or try the most common pattern.
    # Given other sheets use 'Index', Regions likely does too.
    if 'Index' in df_regions.columns:
        df_merged = pd.merge(df_merged, df_regions, left_on='Delivery Region Index', right_on='Index', how='left')
    else:
        # Fallback to direct merge if column names match (unlikely if others didn't)
        # Try to find the index column
        region_key = [col for col in df_regions.columns if 'Index' in col]
        if region_key:
             df_merged = pd.merge(df_merged, df_regions, left_on='Delivery Region Index', right_on=region_key[0], how='left')
    
    # 2. Date Handling
    # Ensure OrderDate is datetime
    if 'OrderDate' in df_merged.columns:
        df_merged['OrderDate'] = pd.to_datetime(df_merged['OrderDate'])
        df_merged['Year'] = df_merged['OrderDate'].dt.year
        df_merged['Month'] = df_merged['OrderDate'].dt.month_name()
        df_merged['Month_Num'] = df_merged['OrderDate'].dt.month
        
    # 3. Calculated Fields (if not already present or needs recalculation)
    # The notebook shows 'Line Total' exists, but let's ensure we have a Profit margin if possible.
    # Total Unit Cost exists in Sales table.
    # Profit = Line Total - (Order Quantity * Total Unit Cost) ? 
    # Let's check column names from notebook inspection:
    # Sales: ['OrderNumber', 'OrderDate', 'Customer Name Index', 'Channel', 'Currency Code', 'Warehouse Code', 'Delivery Region Index', 'Product Description Index', 'Order Quantity', 'Unit Price', 'Line Total', 'Total Unit Cost']
    
    # It seems 'Total Unit Cost' might be per unit or total for the line?
    # Notebook sample: 
    # Order Qty: 6, Unit Price: 2499.1, Line Total: 14994.6 (6*2499.1 = 14994.6) -> Matches
    # Total Unit Cost: 1824.343. 
    # Is 1824.343 the cost per unit or total cost?
    # If partial logic: Margin = Line Total - Total Cost.
    # Let's assume 'Total Unit Cost' in the dataframe is actually "Unit Cost" or "Total Cost for the line".
    # Let's look at the sample again:
    # Row 0: Qty 6, Unit Price 2499.1, Total Unit Cost 1824.343. 
    # If 1824.343 is PER UNIT, then Total Cost = 6 * 1824.343 = 10946.058
    # Profit = 14994.6 - 10946.058 = 4048.54
    # If 1824.343 is TOTAL line cost, then Profit = 14994.6 - 1824.343 = 13170.25 (Very high margin?)
    # Usually "Unit Cost" implies per unit. "Total Unit Cost" is a bit ambiguous naming.
    # Let's calculate a 'Total Cost' column = Order Quantity * Total Unit Cost (assuming it's per unit cost based on the name 'Unit Cost')
    
    # Re-reading notebook cell 65 (head): 
    # Col Name: "Total Unit Cost". Value: 1824.343.
    # Let's assume it IS the unit cost.
    
    df_merged['Total Cost'] = df_merged['Order Quantity'] * df_merged['Total Unit Cost']
    df_merged['Profit'] = df_merged['Line Total'] - df_merged['Total Cost']
    df_merged['Profit Margin'] = (df_merged['Profit'] / df_merged['Line Total']) * 100
    
    return df_merged
