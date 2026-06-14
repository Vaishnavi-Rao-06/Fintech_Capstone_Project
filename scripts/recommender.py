"""
recommender.py

Simple rule-based mutual fund recommendation system.

Takes investor risk appetite (Low/Moderate/High) as input and returns 
the top 3 funds by Sharpe ratio within the matching risk category.

Input: Risk appetite (string) - 'Low', 'Moderate', or 'High'
Output: Printed recommendation table with scheme_name, fund_house, 
        sharpe_ratio, and risk_category
"""

import pandas as pd
from pathlib import Path

PROCESSED_DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"

# Load data
sharpe = pd.read_csv(PROCESSED_DATA_DIR / "sharpe_values.csv")
fund = pd.read_csv(PROCESSED_DATA_DIR / "clean_fund_master.csv")

# Merge sharpe with fund master
merged = sharpe.merge(fund[['amfi_code', 'risk_category']], 
                       on='amfi_code', how='left')

# Risk appetite mapping
risk_mapping = {
    'Low': ['Low'],
    'Moderate': ['Moderate', 'Moderately High'],
    'High': ['High', 'Very High']
}


def recommend_funds(risk_appetite):
    """
    Print top 3 fund recommendations for a given risk appetite.

    Parameters
    ----------
    risk_appetite : str
        One of 'Low', 'Moderate', or 'High'.
    """
    if risk_appetite not in risk_mapping:
        print("Invalid input! Choose: Low, Moderate, High")
        return

    risk_grades = risk_mapping[risk_appetite]

    filtered = merged[merged['risk_category'].isin(risk_grades)]
    top3 = filtered.nlargest(3, 'sharpe_ratio')[
        ['scheme_name', 'fund_house', 'sharpe_ratio', 'risk_category']
    ]

    print(f"\nTop 3 Fund Recommendations for {risk_appetite} Risk Appetite:")
    print("=" * 60)
    print(top3.to_string(index=False))
    print("=" * 60)


if __name__ == "__main__":
    # Test all 3 risk levels
    recommend_funds('Low')
    recommend_funds('Moderate')
    recommend_funds('High')