import pandas as pd

excel_file = "expenditure.xlsx"
df = pd.read_excel(excel_file)
#convert to csv file
csv_file = "new_file.csv"
df.to_csv(csv_file, index=False)
