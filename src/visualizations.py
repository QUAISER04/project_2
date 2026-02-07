import streamlit as st
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
    st.plotly_chart(fig, use_container_width=True)

def plot_sales_by_region(df):
    """
    Plots sales by region.
    Need to ensure 'Region' column exists after merge.
    """
    if 'Region' not in df.columns:
        # Fallback if specific column name is different, usually it's in the Regions sheet
        # Region sheet likely has 'Delivery Region Index' and 'Region' or similar.
        # For now, let's assume the column name from the merge is 'Region' or check available cols.
        # If not, we might need to adjust based on actual column names.
        st.error("Region column not found. Please check data mapping.")
        return

    regional_sales = df.groupby('Region')['Line Total'].sum().reset_index().sort_values('Line Total', ascending=False)
    fig = px.bar(regional_sales, x='Region', y='Line Total', title='Sales by Region', color='Line Total')
    st.plotly_chart(fig, use_container_width=True)

def plot_top_products(df, n=10):
    """
    Plots top N products by sales.
    """
    # Product name column might be 'Product Name' or similar from Products sheet.
    # Let's look for a likely name, or fallback.
    product_col = 'Product Name' if 'Product Name' in df.columns else 'Product Description Index' # Fallback
    
    top_products = df.groupby(product_col)['Line Total'].sum().reset_index().sort_values('Line Total', ascending=False).head(n)
    fig = px.bar(top_products, x='Line Total', y=product_col, orientation='h', title=f'Top {n} Products by Revenue')
    st.plotly_chart(fig, use_container_width=True)

def plot_key_metrics(df):
    """
    Display Key metrics card.
    """
    total_sales = df['Line Total'].sum()
    total_profit = df['Profit'].sum()
    total_orders = df['OrderNumber'].nunique()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"${total_sales:,.2f}")
    col2.metric("Total Profit", f"${total_profit:,.2f}")
    col3.metric("Total Orders", f"{total_orders:,}")
