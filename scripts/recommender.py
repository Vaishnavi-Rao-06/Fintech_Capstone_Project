import pandas as pd

# Load data
sharpe = pd.read_csv("../data/processed/sharpe_values.csv")
fund = pd.read_csv("../data/processed/clean_fund_master.csv")

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
    if risk_appetite not in risk_mapping:
        print("Invalid input! Choose: Low, Moderate, High")
        return
    
    risk_grades = risk_mapping[risk_appetite]
    
    filtered = merged[merged['risk_category'].isin(risk_grades)]
    top3 = filtered.nlargest(3, 'sharpe_ratio')[
        ['scheme_name', 'fund_house', 'sharpe_ratio', 'risk_category']
    ]
    
    print(f"\n Top 3 Fund Recommendations for {risk_appetite} Risk Appetite:")
    print("=" * 60)
    print(top3.to_string(index=False))
    print("=" * 60)

# Test all 3 risk levels
recommend_funds('Low')
recommend_funds('Moderate')
recommend_funds('High')