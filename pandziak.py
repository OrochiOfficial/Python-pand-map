import pandas as pd

# Read data from Excel file
excel_file = 'pow12_22_korekta.xlsx'
df = pd.read_excel(excel_file)

# Display the dataframe (for verification)
print(df)