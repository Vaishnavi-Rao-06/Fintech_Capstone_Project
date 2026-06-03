# Data Dictionary

## clean_fund_master
**Source:** `data/raw/01_fund_master.csv`  
**Rows:** 40 | **Columns:** 15

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | int64 | - |
| fund_house | object | - |
| scheme_name | object | - |
| category | object | - |
| sub_category | object | - |
| plan | object | - |
| launch_date | object | - |
| benchmark | object | - |
| expense_ratio_pct | float64 | - |
| exit_load_pct | float64 | - |
| min_sip_amount | int64 | - |
| min_lumpsum_amount | int64 | - |
| fund_manager | object | - |
| risk_category | object | - |
| sebi_category_code | object | - |

---

## clean_nav
**Source:** `data/raw/02_nav_history.csv`  
**Rows:** 46000 | **Columns:** 3

| Column | Type | Description |
|--------|------|-------------|
| date | object | - |
| amfi_code | int64 | - |
| nav | float64 | - |

---

## clean_aum
**Source:** `data/raw/03_aum_by_fund_house.csv`  
**Rows:** 90 | **Columns:** 5

| Column | Type | Description |
|--------|------|-------------|
| date | object | - |
| fund_house | object | - |
| aum_lakh_crore | float64 | - |
| aum_crore | int64 | - |
| num_schemes | int64 | - |

---

## clean_sip_inflows
**Source:** `data/raw/04_monthly_sip_inflows.csv`  
**Rows:** 48 | **Columns:** 6

| Column | Type | Description |
|--------|------|-------------|
| month | object | - |
| sip_inflow_crore | int64 | - |
| active_sip_accounts_crore | float64 | - |
| new_sip_accounts_lakh | float64 | - |
| sip_aum_lakh_crore | float64 | - |
| yoy_growth_pct | float64 | - |

---

## clean_category_inflows
**Source:** `data/raw/05_category_inflows.csv`  
**Rows:** 144 | **Columns:** 3

| Column | Type | Description |
|--------|------|-------------|
| month | object | - |
| category | object | - |
| net_inflow_crore | float64 | - |

---

## clean_folio_count
**Source:** `data/raw/06_industry_folio_count.csv`  
**Rows:** 21 | **Columns:** 8

| Column | Type | Description |
|--------|------|-------------|
| month | object | - |
| total_folios_crore | float64 | - |
| equity_folios_crore | float64 | - |
| debt_folios_crore | float64 | - |
| hybrid_folios_crore | float64 | - |
| others_folios_crore | float64 | - |
| calculated_total | float64 | - |
| folio_rounding_flag | bool | - |

---

## clean_performance
**Source:** `data/raw/07_scheme_performance.csv`  
**Rows:** 40 | **Columns:** 21

| Column | Type | Description |
|--------|------|-------------|
| Unnamed: 0 | int64 | - |
| amfi_code | int64 | - |
| scheme_name | object | - |
| fund_house | object | - |
| category | object | - |
| plan | object | - |
| return_1yr_pct | float64 | - |
| return_3yr_pct | float64 | - |
| return_5yr_pct | float64 | - |
| benchmark_3yr_pct | float64 | - |
| alpha | float64 | - |
| beta | float64 | - |
| sharpe_ratio | float64 | - |
| sortino_ratio | float64 | - |
| std_dev_ann_pct | float64 | - |
| max_drawdown_pct | float64 | - |
| aum_crore | int64 | - |
| expense_ratio_pct | float64 | - |
| morningstar_rating | int64 | - |
| risk_grade | object | - |
| negative_Sharpe_flag | bool | - |

---

## clean_transactions
**Source:** `data/raw/08_investor_transactions.csv`  
**Rows:** 32778 | **Columns:** 14

| Column | Type | Description |
|--------|------|-------------|
| Unnamed: 0 | int64 | - |
| investor_id | object | - |
| transaction_date | object | - |
| amfi_code | int64 | - |
| transaction_type | object | - |
| amount_inr | int64 | - |
| state | object | - |
| city | object | - |
| city_tier | object | - |
| age_group | object | - |
| gender | object | - |
| annual_income_lakh | float64 | - |
| payment_mode | object | - |
| kyc_status | object | - |

---

## clean_portfolio_holdings
**Source:** `data/raw/09_portfolio_holdings.csv`  
**Rows:** 322 | **Columns:** 8

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | int64 | - |
| stock_symbol | object | - |
| stock_name | object | - |
| sector | object | - |
| weight_pct | float64 | - |
| market_value_cr | float64 | - |
| current_price_inr | float64 | - |
| portfolio_date | object | - |

---

## clean_benchmark_indices
**Source:** `data/raw/10_benchmark_indices.csv`  
**Rows:** 8050 | **Columns:** 3

| Column | Type | Description |
|--------|------|-------------|
| date | object | - |
| index_name | object | - |
| close_value | float64 | - |

---

