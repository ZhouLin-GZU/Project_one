import pandas as pd
filePath_01 ='F:\file2\MyProject\File\data_01.xlsx'
df_01 = pd.read_excel(filePath_01,sheet_name = 'sheet1')
print(df_01)