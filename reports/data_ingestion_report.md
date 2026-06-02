#DATA INGESTION REPORT

##Dataset 1: Fund Master 
-Anomalies:
>> launch_date is stored as str instead of datetime.
>> Several categorical columns are correctly stored in object and str datatypes.

##Dataset 2: NAV History 
-Anomalies:
>> date is stored as str instead of datetime.
>> Large dataset with 46,000 records, suitable for trend analysis
>> date conversion will be needed for time-series analysis.

##Dataset 3: AUM by Fund House
-Anomalies:
>> date column is stored as string.
>> No obvious datatype issues.

##Dataset 4: Monthly SIP Inflows 
-Anomalies:
>> month stored as string.
>> yoy_growth_pct contains missing values (NaN) in initial rows.
>> Missing values appear expected because year-over-year growth cannot be calculated for early periods.

##Dataset 5: Category Inflows 
-Anomalies:
>> month stored as string.
>> No obvious missing values visible in sample.(required deeper analysis to confirm)

##Dataset 6: Industry Folio Count
-Anomalies:
>> month stored as string.
>> Numerical columns appear correctly typed.

##Dataset 7: Scheme Performance 
-Anomalies:
>> Large number of performance metrics.
>> risk_grade stored as text, which is expected.
>> No immediate datatype inconsistencies observed.

##Dataset 8: Investor Transactions 
-Anomalies:
>> transaction_date stored as string instead of datetime.
>> Multiple categorical fields may require encoding for modeling.

##Dataset 9: Portfolio Holdings
-Anomalies:
>> portfolio_date stored as string instead of datetime.
>> No other datatype issues observed.

##Dataset 10: Benchmark Indices 
-Anomalies:
>> date stored as string instead of datetime.
>> Suitable for time-series analysis after date conversion.

##Cross-Dataset Observation :
>> Multiple datasets contain date-like fields stored as strings.
>> Standardization to datetime format is required across all datasets to ensure consistent time-series analysis and aggregation.
>> Key observations include missing values in the yoy_growth_pct column, significant variation in dataset sizes, and the presence of high-cardinality categorical attributes.
>> The datasets appear interconnected through common identifiers such as amfi_code, suggesting they can be integrated for comprehensive financial analysis. 
>> Further validation for duplicates, missing values, and outliers will be conducted during the data cleaning phase.