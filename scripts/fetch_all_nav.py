import requests
import pandas as pd
    
schemes = {
        "SBI_Bluechip":119551,
        "ICICI_Bluechip":120503,
        "Nippon_Largecap":118632,
        "Axis_Bluechip":119092,
        "Kotak_Bluechip":120841
    }
    
for name, code in schemes.items():
        response = requests.get(f"https://api.mfapi.in/mf/{code}")
        data = response.json()
        
        df = pd.DataFrame(data["data"])
        df.to_csv(f"C:/Users/vaishnavi/Downloads/Fintech_Capstone_Project/data/raw/{name}_nac.csv",index=False)
        
        print(f"Done. {name} - {len(df)} rows saved.")
        