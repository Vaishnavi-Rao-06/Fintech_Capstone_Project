"""
app.py

Streamlit web app — Bluestock MF Analytics Dashboard
An interactive alternative to the Power BI dashboard, built using 
Streamlit and Plotly, reading from the cleaned CSV datasets.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Bluestock MF Analytics", layout="wide")

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"

@st.cache_data
def load_data():
    fund = pd.read_csv(DATA_DIR / "clean_fund_master.csv")
    nav = pd.read_csv(DATA_DIR / "clean_nav.csv")
    nav['date'] = pd.to_datetime(nav['date'])
    aum = pd.read_csv(DATA_DIR / "clean_aum.csv")
    aum['date'] = pd.to_datetime(aum['date'])
    sip = pd.read_csv(DATA_DIR / "clean_sip_inflows.csv")
    sip['month'] = pd.to_datetime(sip['month'])
    cat = pd.read_csv(DATA_DIR / "clean_category_inflows.csv")
    cat['month'] = pd.to_datetime(cat['month'])
    txn = pd.read_csv(DATA_DIR / "clean_transactions.csv")
    txn['transaction_date'] = pd.to_datetime(txn['transaction_date'])
    folio = pd.read_csv(DATA_DIR / "clean_folio_count.csv")
    folio['month'] = pd.to_datetime(folio['month'])
    perf = pd.read_csv(DATA_DIR / "clean_performance.csv")
    benchmark = pd.read_csv(DATA_DIR / "clean_benchmark_indices.csv")
    benchmark['date'] = pd.to_datetime(benchmark['date'])
    return fund, nav, aum, sip, cat, txn, folio, perf, benchmark

fund, nav, aum, sip, cat, txn, folio, perf, benchmark = load_data()

st.title("Bluestock MF Analytics")
st.markdown("### Mutual Fund Industry Analysis Dashboard")

tab1, tab2, tab3, tab4 = st.tabs([
    " Industry Overview", 
    " Fund Performance", 
    " Investor Analytics", 
    " SIP & Market Trends"
])

# ==================== TAB 1: INDUSTRY OVERVIEW ====================
with tab1:
    st.subheader("Industry Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total AUM (Cr)", f"{aum['aum_crore'].sum():,.0f}")
    col2.metric("SIP Inflows (Cr)", f"{sip['sip_inflow_crore'].sum():,.0f}")
    col3.metric("Total Folios (Cr)", f"{folio['total_folios_crore'].sum():.2f}")
    col4.metric("Total Schemes", fund['amfi_code'].nunique())
    
    col1, col2 = st.columns(2)
    
    with col1:
        aum_yearly = aum.copy()
        aum_yearly['year'] = aum_yearly['date'].dt.year
        aum_by_year = aum_yearly.groupby('year')['aum_crore'].sum().reset_index()
        fig = px.line(aum_by_year, x='year', y='aum_crore', 
                       title='Industry AUM Growth (2022-2025)', markers=True)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        aum_by_house = aum.groupby('fund_house')['aum_crore'].sum().nlargest(10).reset_index()
        fig = px.bar(aum_by_house, x='aum_crore', y='fund_house', 
                      orientation='h', title='Top 10 Fund Houses by AUM')
        fig.update_layout(yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
# ==================== TAB 2: FUND PERFORMANCE ====================
with tab2:
    st.subheader("Fund Performance")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        fund_house_filter = st.multiselect("Fund House", 
            options=fund['fund_house'].unique(), default=None)
    with col2:
        category_filter = st.multiselect("Category", 
            options=fund['category'].unique(), default=None)
    with col3:
        plan_filter = st.multiselect("Plan", 
            options=fund['plan'].unique(), default=None)
    
    # Apply filters
    filtered_fund = fund.copy()
    if fund_house_filter:
        filtered_fund = filtered_fund[filtered_fund['fund_house'].isin(fund_house_filter)]
    if category_filter:
        filtered_fund = filtered_fund[filtered_fund['category'].isin(category_filter)]
    if plan_filter:
        filtered_fund = filtered_fund[filtered_fund['plan'].isin(plan_filter)]
    
    filtered_perf = perf[perf['amfi_code'].isin(filtered_fund['amfi_code'])]
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.scatter(filtered_perf, x='return_3yr_pct', y='std_dev_ann_pct',
                          size='aum_crore', color='fund_house',
                          hover_name='scheme_name',
                          title='Return vs Risk (Bubble = AUM)')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Fund selector for NAV chart
        selected_fund = st.selectbox("Select Fund for NAV Chart", 
            options=filtered_fund['scheme_name'].unique())
        selected_code = filtered_fund[filtered_fund['scheme_name'] == selected_fund]['amfi_code'].iloc[0]
        
        fund_nav = nav[nav['amfi_code'] == selected_code]
        nifty100 = benchmark[benchmark['index_name'] == 'NIFTY100']
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=fund_nav['date'], y=fund_nav['nav'], 
                                  name='NAV', yaxis='y1'))
        fig.add_trace(go.Scatter(x=nifty100['date'], y=nifty100['close_value'], 
                                  name='NIFTY100', yaxis='y2'))
        fig.update_layout(
            title=f'NAV vs Benchmark — {selected_fund[:30]}',
            yaxis=dict(title='NAV'),
            yaxis2=dict(title='NIFTY100', overlaying='y', side='right')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("#### Fund Scorecard")
    scorecard_display = filtered_perf[['scheme_name', 'fund_house', 'return_3yr_pct', 
                                         'sharpe_ratio', 'aum_crore', 'expense_ratio_pct']]
    st.dataframe(scorecard_display.sort_values('sharpe_ratio', ascending=False), 
                  use_container_width=True)
# ==================== TAB 3: INVESTOR ANALYTICS ====================
with tab3:
    st.subheader("Investor Analytics")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        state_filter = st.multiselect("State", options=txn['state'].unique(), default=None)
    with col2:
        age_filter = st.multiselect("Age Group", options=txn['age_group'].unique(), default=None)
    with col3:
        tier_filter = st.multiselect("City Tier", options=txn['city_tier'].unique(), default=None)
    
    filtered_txn = txn.copy()
    if state_filter:
        filtered_txn = filtered_txn[filtered_txn['state'].isin(state_filter)]
    if age_filter:
        filtered_txn = filtered_txn[filtered_txn['age_group'].isin(age_filter)]
    if tier_filter:
        filtered_txn = filtered_txn[filtered_txn['city_tier'].isin(tier_filter)]
    
    col1, col2 = st.columns(2)
    
    with col1:
        state_data = filtered_txn.groupby('state')['amount_inr'].sum().reset_index()
        state_data = state_data.sort_values('amount_inr', ascending=True)
        fig = px.bar(state_data, x='amount_inr', y='state', orientation='h',
                      title='Transaction Amount by State')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        type_data = filtered_txn['transaction_type'].value_counts().reset_index()
        type_data.columns = ['transaction_type', 'count']
        fig = px.pie(type_data, values='count', names='transaction_type',
                      title='Transaction Type Split', hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        age_sip = filtered_txn.groupby('age_group')['amount_inr'].mean().reset_index()
        fig = px.bar(age_sip, x='age_group', y='amount_inr',
                      title='Avg SIP Amount by Age Group')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        monthly_vol = filtered_txn.groupby(filtered_txn['transaction_date'].dt.to_period('M')).size().reset_index()
        monthly_vol.columns = ['month', 'count']
        monthly_vol['month'] = monthly_vol['month'].astype(str)
        fig = px.line(monthly_vol, x='month', y='count',
                       title='Monthly Transaction Volume')
        st.plotly_chart(fig, use_container_width=True) 
# ==================== TAB 4: SIP & MARKET TRENDS ====================
with tab4:
    st.subheader("SIP & Market Trends")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nifty50 = benchmark[benchmark['index_name'] == 'NIFTY50']
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=sip['month'], y=sip['sip_inflow_crore'], 
                              name='SIP Inflow (Cr)', yaxis='y1'))
        fig.add_trace(go.Scatter(x=nifty50['date'], y=nifty50['close_value'], 
                                  name='NIFTY 50', yaxis='y2', line=dict(color='orange')))
        fig.update_layout(
            title='SIP Inflow vs NIFTY 50 (2022-2025)',
            yaxis=dict(title='SIP Inflow (Cr)'),
            yaxis2=dict(title='NIFTY 50', overlaying='y', side='right')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        top5_cat = cat.groupby('category')['net_inflow_crore'].sum().nlargest(5).reset_index()
        fig = px.bar(top5_cat, x='net_inflow_crore', y='category', orientation='h',
                      title='Top 5 Categories by Net Inflow')
        fig.update_layout(yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("New SIP Accounts (Lakh)", f"{sip['new_sip_accounts_lakh'].sum():,.2f}")
    
    with col2:
        st.metric("Latest SIP Inflow (Cr)", f"{sip['sip_inflow_crore'].iloc[-1]:,.0f}")
    
    st.markdown("#### Category Inflows by Month")
    cat_pivot = cat.pivot_table(index='category', columns=cat['month'].dt.strftime('%Y-%m'), 
                                  values='net_inflow_crore', aggfunc='sum')
    st.dataframe(cat_pivot, use_container_width=True)

st.markdown("---")
st.markdown("**Bluestock MF Analytics** — Capstone Project | Built with Streamlit & Plotly")   