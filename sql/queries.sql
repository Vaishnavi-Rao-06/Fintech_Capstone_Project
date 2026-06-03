-- 1. Top 5 funds by aum
SELECT scheme_name, fund_house, aum_crore
FROM fact_performance
OREDER BY aum_crore DESC
LIMIT 5;

-- 2. Average nav per month
SELECT 
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

--3.  SIP inflow yoy growth
SELECT month, sip_inflow_crore, yoy_growth_pct
FROM sip_inflows
ORDER BY month;

--4. Transactions by state
SELECT state,
       COUNT(*) AS total_transactions,
       ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total transactions DESC;

--5. Funds with expense ration <1%
SELECT scheme_name, fund_house, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct <1.0
ORDER BY expense_ratio_pct ASC;

--6. Top 5 funds by 3 year return
SELECT scheme_name, fund_house, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

--7. Funds with negative sharpe ratio
SELECT scheme_name, fund_house, sharpe_ratio
FROM fact_performance
WHERE sharpe_ratio<0
ORDER BY sharpe_ratio ASC;

--8. Transaction count by type
SELECT transaction_type,
       COUNT(*) AS total_transactions,
       ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;

--9. Category wise net inflows
SELECT category,
       ROUND(SUM(net_inflow_crore),2) AS total_inflow
FROM category_inflows
GROUP BY category
ORDER BY total_inflow DESC;

--10. Top 5 performing funds vs benchmark
SELECT scheme_name. fund_house,
       return_3yr_pct, benchmark_3yr_pct,
       ROUND(return_3yr_pct - benchmark_3yr_pct,2) AS alpha_over_benchmark
FROM fact_performance
WHERE return_3yr_pct > benchmark_3yr_pct
ORDER BY alpha_over_benchmark DESC
LIMIT 5;
