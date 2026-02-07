import streamlit as st
import pandas as pd
from src.data_loader import load_data, clean_data
from src.visualizations import plot_sales_trend, plot_sales_by_region, plot_top_products, plot_key_metrics

# Page Config
st.set_page_config(page_title="Sales Domain", layout="wide")

# Title
st.title("📊 Sales Domain")
st.markdown("Interactive dashboard to explore sales performance, trends, and profitability.")

# Load Data
@st.cache_data
def get_data():
    filepath = "data/Regional Sales Dataset.xlsx"
    sheets = load_data(filepath)
    if sheets:
        df = clean_data(sheets)
        return df
    return None

df = get_data()

if df is not None:
    # Sidebar - Filters
    st.sidebar.header("Filters")
    
    # Year Filter
    years = sorted(df['Year'].unique())
    selected_year = st.sidebar.multiselect("Select Year", years, default=years)
    
    # Region Filter (if available)
    if 'Region' in df.columns:
        regions = sorted(df['Region'].astype(str).unique())
        selected_region = st.sidebar.multiselect("Select Region", regions, default=regions)
    else:
        selected_region = []
        
    # Apply Filters
    df_filtered = df.copy()
    if selected_year:
        df_filtered = df_filtered[df_filtered['Year'].isin(selected_year)]
    if selected_region and 'Region' in df.columns:
        df_filtered = df_filtered[df_filtered['Region'].isin(selected_region)]
        
    # Main Dashboard
    
    # 1. Key Metrics
    st.subheader("Key Performance Indicators")
    plot_key_metrics(df_filtered)
    
    st.markdown("---")
    
    # 2. Charts Row 1
    col1, col2 = st.columns(2)
    
    with col1:
        plot_sales_trend(df_filtered)
        
    with col2:
        if 'Region' in df.columns:
            plot_sales_by_region(df_filtered)
        else:
            st.info("Region data not available for plotting.")

    # 3. Charts Row 2
    st.markdown("---")
    plot_top_products(df_filtered)
    
    # 4. Data Table
    with st.expander("View Raw Data"):
        st.dataframe(df_filtered.head(100))
        
else:
    st.error("Failed to load data. Please check if 'data/Regional Sales Dataset.xlsx' exists.")
