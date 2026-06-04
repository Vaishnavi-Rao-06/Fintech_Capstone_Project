
import requests
import pandas as pd

response = requests.get("https://api.mfapi.in/mf/125497")
data = response.json()

df = pd.DataFrame(data["data"])
df.to_csv("C:/Users/vaishnavi/Downloads/Fintech_Capstone_Project/data/raw/hdfc_top100_nav.csv",index=False)

print(f"Done. {len(df)} rows saved.")
print(df.head())
