# Bluestock MF Analytics — Capstone Project

A comprehensive data analytics project on the Indian Mutual Fund industry, 
covering ETL, EDA, performance metrics, risk analysis, and an interactive 
Power BI dashboard.

## 📌 Project Overview

This project analyzes 40 mutual fund schemes across 10 fund houses (2022-2026), 
using data from AMFI and live NAV data from mfapi.in. It covers the full 
data pipeline: ingestion → cleaning → SQL database → EDA → performance 
analytics → advanced risk analytics → interactive dashboard → final report.

## 📁 Folder Structure
  Fintech_Capstone_Project/

├── data/

│   ├── raw/           # Original downloaded files

│   ├── processed/     # Cleaned, merged CSVs

│   └── db/             # bluestock_mf.db (SQLite) - not tracked in git

├── notebooks/          # Jupyter notebooks for each stage

├── scripts/            # Python ETL and utility scripts

├── sql/                 # Schema and queries

├── dashboard/           # Power BI dashboard file

├── reports/             # Final report, presentation, charts

└── README.md~
## 🛠️ Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Vaishnavi-Rao-06/Fintech_Capstone_Project.git
cd Fintech_Capstone_Project
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 How to Run

### Run ETL / Data Ingestion
```bash
cd scripts
python data_ingestion.py
python live_nav_fetch.py
python fetch_all_nav.py
```

### Run Fund Recommender
```bash
cd scripts
python recommender.py
```

### Run Notebooks
Open Jupyter and run notebooks in order:
```bash
cd notebooks
jupyter notebook
```
Recommended order: fund master EDA → cleaning notebooks → 
`03_eda_analysis.ipynb` → `04_performance_analytics.ipynb` → 
`05_advanced_analytics.ipynb`

### Open Dashboard
Open `dashboard/bluestock_mf_dashboard.pbix` in Power BI Desktop.

## 📊 Key Deliverables

| Deliverable | Location |
|------------|----------|
| Cleaned datasets (10 CSVs) | `data/processed/` |
| SQLite database | `data/db/bluestock_mf.db` |
| Database schema | `sql/schema.sql` |
| SQL queries + results | `sql/queries.sql`, `sql/query_results.txt` |
| EDA notebook (15+ charts) | `notebooks/03_eda_analysis.ipynb` |
| Performance metrics | `notebooks/04_performance_analytics.ipynb` |
| Advanced analytics | `notebooks/05_advanced_analytics.ipynb` |
| Power BI dashboard (4 pages) | `dashboard/bluestock_mf_dashboard.pbix` |
| Final report | `reports/Final_Report.pdf` |
| Presentation | `reports/Bluestock_MF_Presentation.pptx` |
| Data dictionary | `reports/data_dictionary.md` |

## 📈 Key Findings

- SBI Mutual Fund dominates industry AUM with ~₹12.5L Crore
- Monthly SIP inflows hit all-time high of ₹31,002 Crore (Dec 2025)
- Total folios doubled from 13.26 Cr to 26.12 Cr (2022-2025)
- Mirae Asset Large Cap Fund leads risk-adjusted returns (Sharpe: 1.45)
- B30 cities represent significant untapped growth opportunity

## Author:

**Vaishnavi Rao**

## 🎁 Bonus Challenges Completed (+50 marks)

| # | Challenge | Deliverable |
|---|-----------|-------------|
| B1 | Scheduled ETL (Windows Task Scheduler) | `reports/B1_cron_setup.md` |
| B2 | Streamlit Web App (alternative to Power BI) | `dashboard/app.py` — run with `streamlit run app.py` |
| B3 | Monte Carlo NAV Simulation (5yr projection) | `data/processed/monte_carlo_results.csv`, `reports/charts/monte_carlo_simulation.png` |
| B4 | Markowitz Efficient Frontier | `data/processed/efficient_frontier_portfolios.csv`, `reports/charts/efficient_frontier.png` |
| B5 | Automated HTML Email Report | `scripts/email_report.py`, `reports/weekly_email_report.html` |

All bonus analyses are documented in `notebooks/05_advanced_analytics.ipynb` 
and `notebooks/06_monte_carlo_simulation.ipynb`.
