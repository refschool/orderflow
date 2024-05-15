#https://github.com/matplotlib/mplfinance/issues/136


import numpy as np
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

Index= ['0', '1', '2', '3', '4']
Cols = ['A']
df = DataFrame([1,2,1,3,8], index=Index, columns=Cols)
print(df)
sns.heatmap(df, annot=True)
plt.show()