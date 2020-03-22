import pandas as pd

Datas = pd.read_csv("Parameters.csv",index_col=0)
print(Datas)
print(int(Datas.loc["M_s"]*10))
