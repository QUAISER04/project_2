# 📊 Sales Domain

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)

A professional, interactive dashboard designed to transform raw sales data into actionable business insights. This project uses Streamlit to visualize trends, regional performance, and product success.

---

## 🚀 Key Features

*   **📈 Dynamic Trends**: Visualize how sales and profit margins evolve over time.
*   **🌍 Regional Insights**: Drill down into performance by specific regions.
*   **🏆 Product Rankings**: Instantly identify your top-selling items.
*   **⚡ Interactive Filters**: Slice and dice data by Year and Region in real-time.

## 🛠️ Tech Stack

*   **Logic**: Python (Pandas, Numpy)
*   **Visualization**: Plotly Express
*   **Interface**: Streamlit

## 📂 Project Structure

```text
├── app.py                  # The main application dashboard (ENTRY POINT)
├── src/
│   ├── data_loader.py      # Handles data loading & cleaning
│   └── visualizations.py   # Charting logic
├── data/                   # Stores source datasets
└── requirements.txt        # Project dependencies
```

## 🏁 Getting Started

Follow these simple steps to run the dashboard on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com/QUAISER04/project_2.git
cd project_2
```

### 2. Install Dependencies
It's recommended to use a virtual environment:
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install libraries
pip install -r requirements.txt
```

### 3. Run the Dashboard
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

## ☁️ Deployment

When deploying to Streamlit Cloud:
1.  **Repository**: Select `QUAISER04/project_2`.
2.  **Branch**: `main`.
3.  **Main file path**: Ensure this is set to `app.py`.  
    *(Note: If it defaults to `src/visualizations.py`, change it manually or the app will not load.)*

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas for improvements.

## 📄 License

This project is open-source and available for educational purposes.
