



import pandas as pd
import bioinfokit
from bioinfokit import analys, visuz
import numpy as np

file_path = r'C:\Users\aram\Desktop\ms data analysis python\mutual volcano.csv'

# Load the Excel file
df = pd.read_csv(file_path)
df.head()
print(df.head())
df.shape
print(df.shape)
bioinfokit.visuz.GeneExpression.volcano
print(bioinfokit.visuz.GeneExpression.volcano)
print(bioinfokit.visuz.GeneExpression.volcano(df=df,lfc='log2fc',pv='p_val',geneid='proteins',genenames='deg',plotlegend=True,legendpos='upper right',lfc_thr=(1,1),pv_thr=(0.06,0.06),show=True))
