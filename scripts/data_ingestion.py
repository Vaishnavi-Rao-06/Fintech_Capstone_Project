"""
data_ingestion.py

Loads all 10 raw CSV datasets and prints shape, dtypes, and head() 
for each — used for initial data exploration during Day 1.

Input: 10 CSV files in data/raw/
Output: Printed summaries (shape, dtypes, head) for each dataset
"""

import pandas as pd
from pathlib import Path

RAW_DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

datasets = {
    "Fund Master": "01_fund_master.csv",
    "NAV History": "02_nav_history.csv",
    "AUM by Fund House": "03_aum_by_fund_house.csv",
    "Monthly SIP Inflows": "04_monthly_sip_inflows.csv",
    "Category Inflows": "05_category_inflows.csv",
    "Industry Folio Count": "06_industry_folio_count.csv",
    "Scheme Performance": "07_scheme_performance.csv",
    "Investor Transactions": "08_investor_transactions.csv",
    "Portfolio Holdings": "09_portfolio_holdings.csv",
    "Benchmark Indices": "10_benchmark_indices.csv",
}

for name, filename in datasets.items():
    df = pd.read_csv(RAW_DATA_DIR / filename)
    print(f"\n{'='*50}")
    print(f"{name} ({filename})")
    print('='*50)
    print(df.head())
    print(f"Shape: {df.shape}")
    print(f"Dtypes:\n{df.dtypes}")