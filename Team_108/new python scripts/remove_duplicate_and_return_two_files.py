import pandas as pd
import numpy as np

excel_file1 ='book1.xlsx'
excel_file2 ='book2.xlsx'

file_df1 = pd.read_excel(excel_file1)
file_df2 = pd.read_excel(excel_file2)

source_df1 = pd.DataFrame(file_df1)
source_df2 = pd.DataFrame(file_df2)

print('Source DataFrame1:\n', source_df1)
print('Source DataFrame2:\n', source_df2)



df = pd.concat([source_df1, source_df2])

df.duplicated()
df.loc[df.duplicated(), :]
df.loc[df.duplicated(keep=False), :]
df = df.loc[df.duplicated(keep=False), :]


result_df = df.drop_duplicates()
print('Result DataFrame:\n', result_df)

result_df.to_excel("my_excel_file.xlsx")
result_df.to_excel("my_excel_file1.xlsx")















