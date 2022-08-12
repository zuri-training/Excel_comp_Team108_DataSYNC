
import pandas as pd
import numpy as np

excel_file = 'trial1.xlsx'

file_df = pd.read_excel(excel_file)
source_df = pd.DataFrame(file_df)

print('Source DataFrame:\n', source_df)

result_df = source_df.drop_duplicates()

print('Result DataFrame:\n', result_df)

result_df.to_excel("my_excel_file1.xlsx")