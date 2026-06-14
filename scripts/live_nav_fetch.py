"""
live_nav_fetch.py

Fetches live NAV (Net Asset Value) data for HDFC Top 100 Direct Plan 
(AMFI code: 125497) from the mfapi.in REST API.

Parses the JSON response and saves the NAV history as a raw CSV file 
in data/raw/hdfc_top100_nav.csv.

Input: None (API call)
Output: data/raw/hdfc_top100_nav.csv
"""

import requests
import pandas as pd

response = requests.get("https://api.mfapi.in/mf/125497")
data = response.json()

df = pd.DataFrame(data["data"])
df.to_csv("C:/Users/vaishnavi/Downloads/Fintech_Capstone_Project/data/raw/hdfc_top100_nav.csv",index=False)

print(f"Done. {len(df)} rows saved.")
print(df.head())
