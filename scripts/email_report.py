"""
email_report.py

Generates an automated HTML email report summarizing weekly mutual 
fund performance — top gainers, SIP inflows, and key metrics.

This script generates the HTML report and saves it locally. To 
actually send via email, configure SMTP credentials (see bottom 
of file for instructions).

Output: reports/weekly_email_report.html
"""

import pandas as pd
from pathlib import Path
from datetime import datetime

PROCESSED_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"
REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports"

# Load data
perf = pd.read_csv(PROCESSED_DIR / "clean_performance.csv")
sip = pd.read_csv(PROCESSED_DIR / "clean_sip_inflows.csv")
scorecard = pd.read_csv(PROCESSED_DIR / "fund_scorecard.csv")

# Top 5 funds by composite score
top5 = scorecard.head(5)

# Latest SIP data
latest_sip = sip.iloc[-1]

# Top 3 gainers (1yr return)
top_gainers = perf.nlargest(3, 'return_1yr_pct')[['scheme_name', 'fund_house', 'return_1yr_pct']]

# Build HTML
html = f"""
<html>
<head>
<style>
    body {{ font-family: Arial, sans-serif; background-color: #f4f6f9; padding: 20px; }}
    .container {{ max-width: 700px; margin: auto; background: white; padding: 30px; border-radius: 8px; }}
    h1 {{ color: #1a3c5e; }}
    h2 {{ color: #4a6fa5; border-bottom: 2px solid #e0e0e0; padding-bottom: 5px; }}
    table {{ width: 100%; border-collapse: collapse; margin: 10px 0; }}
    th {{ background-color: #1a3c5e; color: white; padding: 8px; text-align: left; }}
    td {{ padding: 8px; border-bottom: 1px solid #e0e0e0; }}
    .metric {{ display: inline-block; background: #f0f4f8; padding: 15px; margin: 5px; border-radius: 6px; text-align: center; }}
    .metric-value {{ font-size: 24px; font-weight: bold; color: #1a3c5e; }}
    .footer {{ color: #999; font-size: 12px; margin-top: 20px; text-align: center; }}
</style>
</head>
<body>
<div class="container">
    <h1>📊 Bluestock MF Weekly Report</h1>
    <p>Week of {datetime.now().strftime('%B %d, %Y')}</p>
    
    <h2>Key Metrics</h2>
    <div class="metric">
        <div class="metric-value">₹{latest_sip['sip_inflow_crore']:,.0f} Cr</div>
        <div>Latest SIP Inflow</div>
    </div>
    <div class="metric">
        <div class="metric-value">{latest_sip['new_sip_accounts_lakh']:.1f} L</div>
        <div>New SIP Accounts</div>
    </div>
    
    <h2>🏆 Top 5 Funds (Composite Score)</h2>
    <table>
        <tr><th>Scheme</th><th>Fund House</th><th>3yr CAGR</th><th>Sharpe</th><th>Score</th></tr>
"""

for _, row in top5.iterrows():
    html += f"""
        <tr>
            <td>{row['scheme_name'][:30]}</td>
            <td>{row['fund_house']}</td>
            <td>{row['cagr_3yr']:.2f}%</td>
            <td>{row['sharpe_ratio']:.2f}</td>
            <td>{row['composite_score']:.2f}</td>
        </tr>
    """

html += """
    </table>
    
    <h2>📈 Top 3 Gainers (1yr Return)</h2>
    <table>
        <tr><th>Scheme</th><th>Fund House</th><th>1yr Return</th></tr>
"""

for _, row in top_gainers.iterrows():
    html += f"""
        <tr>
            <td>{row['scheme_name'][:30]}</td>
            <td>{row['fund_house']}</td>
            <td>{row['return_1yr_pct']:.2f}%</td>
        </tr>
    """

html += """
    </table>
    
    <div class="footer">
        Generated automatically by Bluestock MF Analytics<br>
        This is an automated report. Data sourced from AMFI and mfapi.in
    </div>
</div>
</body>
</html>
"""

# Save HTML
output_path = REPORTS_DIR / "weekly_email_report.html"
with open(output_path, "w") as f:
    f.write(html)

print(f"✅ HTML report saved to {output_path}")

# ============================================
# TO ACTUALLY SEND VIA EMAIL (uncomment & configure):
# ============================================
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # Use Gmail App Password
RECEIVER_EMAIL = "recipient@example.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = 'Bluestock MF Weekly Report'
msg['From'] = SENDER_EMAIL
msg['To'] = RECEIVER_EMAIL
msg.attach(MIMEText(html, 'html'))

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)

print("Email sent successfully!")
"""