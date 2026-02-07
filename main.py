import pandas as pd
from src.data_loader import load_data, clean_data
from src.visualizations import plot_sales_trend, plot_sales_by_region, plot_top_products, plot_key_metrics

def main():
    print("Loading data...")
    filepath = "data/Regional Sales Dataset.xlsx"
    sheets = load_data(filepath)
    
    if sheets:
        df = clean_data(sheets)
        
        # Display Metrics
        plot_key_metrics(df)
        
        # Display Charts
        print("\nGenering charts... (Check your browser/window)")
        plot_sales_trend(df)
        
        if 'Region' in df.columns:
            plot_sales_by_region(df)
        
        plot_top_products(df)
        
    else:
        print("Failed to load data.")

if __name__ == "__main__":
    main()
