import pandas as pd

excel_file = "unique505.xlsx"
selected_columns = ['Topic', 'title']

df = pd.read_excel(excel_file, usecols=selected_columns)

csv_output = "topics.csv"

df.to_csv(csv_output, index=False)