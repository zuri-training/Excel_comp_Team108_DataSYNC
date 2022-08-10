import pandas as pd 
import numpy as np

file_df=pd.read_excel()

source_df = pd.DataFrame(file_df)
print('Source DataFrame:\n', source_df)

#keep first duplicate row
result_df = source_df.drop_duplicates( )
print('Result DataFrame:\n', result_df)
result_df.to_excel()