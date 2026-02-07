# 📊 Sales Analysis Dashboard

A simple and interactive dashboard to explore sales data, analyze trends, and view top-performing products.

## Features
- **Sales Trends**: See how sales have changed over time (monthly/yearly).
- **Regional Analysis**: View sales performance by region.
- **Top Products**: Identify the best-selling products.
- **Key Metrics**: actionable insights on Total Sales, Profit, and Orders.

## How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com/QUAISER04/project_2.git
   cd project_2
   ```

2. **Set up the environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the App:**
   ```bash
   streamlit run app.py
   ```

## Project Structure
- `app.py`: The main application file.
- `data/`: Contains the Excel dataset.
- `src/`: Contains code for loading data and creating charts.
