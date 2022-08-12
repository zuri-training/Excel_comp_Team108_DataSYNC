import pandas as pd 
import numpy as np

excel_file = 'book1.xlsx'

df = pd.read_excel(excel_file)
df.duplicated()
df.loc[df.duplicated(), :]


df = df.loc[df.duplicated(), :]

# function definition
def highlight_cols(x):
      
    # copy df to new - original data is not changed
    df = x.copy()
      
    # select all values to yellow color
    df.loc[:, :] = 'background-color: yellow'
      
    # return color df
    return df 
  
print("Highlighted DataFrame :")
display = (df.style.apply(highlight_cols, axis = None))

display.to_excel("my_excel_file.xlsx")


