import plotly.express as px
import pandas as pd

def plot_sales_trend(df):
    """
    Plots monthly sales trend using Plotly.
    """
    # Group by Year-Month
    monthly_sales = df.groupby(['Year', 'Month_Num', 'Month'])['Line Total'].sum().reset_index()
    monthly_sales = monthly_sales.sort_values(['Year', 'Month_Num'])
    monthly_sales['Year-Month'] = monthly_sales['Year'].astype(str) + '-' + monthly_sales['Month']
    
    fig = px.line(monthly_sales, x='Year-Month', y='Line Total', title='Monthly Sales Trend', markers=True)
    fig.show()

def plot_sales_by_region(df):
    """
    Plots sales by region.
    """
    if 'Region' not in df.columns:
        print("Region column not found. Please check data mapping.")
        return

    regional_sales = df.groupby('Region')['Line Total'].sum().reset_index().sort_values('Line Total', ascending=False)
    fig = px.bar(regional_sales, x='Region', y='Line Total', title='Sales by Region', color='Line Total')
    fig.show()

def plot_top_products(df, n=10):
    """
    Plots top N products by sales.
    """
    product_col = 'Product Name' if 'Product Name' in df.columns else 'Product Description Index' # Fallback
    
    top_products = df.groupby(product_col)['Line Total'].sum().reset_index().sort_values('Line Total', ascending=False).head(n)
    fig = px.bar(top_products, x='Line Total', y=product_col, orientation='h', title=f'Top {n} Products by Revenue')
    fig.show()

def plot_key_metrics(df):
    """
    Display Key metrics card.
    """
    total_sales = df['Line Total'].sum()
    total_profit = df['Profit'].sum()
    total_orders = df['OrderNumber'].nunique()
    
    print("-" * 30)
    print("KEY PERFORMANCE INDICATORS")
    print("-" * 30)
    print(f"Total Sales : ${total_sales:,.2f}")
    print(f"Total Profit: ${total_profit:,.2f}")
    print(f"Total Orders: {total_orders:,}")
    print("-" * 30)
