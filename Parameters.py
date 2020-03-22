import numpy as np
import pandas as pd

Datas = pd.DataFrame(data=[2000,10**12,10**4,10**-4,200,10,10**9,10**4,2*10**-4,200,100], index=["R_g","M_s","n_s","z_s","R_s_s","R_c","M_c","n_c","z_c","R_c_s","N_c"], columns=["Value"])


'''
Title = ["R_g","M_s","n_s","z_s","R_s_s","R_c","M_c","n_c","z_c","R_c_s","N_c"]
Value = [2000,10**12,10**4,10**-4,200,10,10**9,10**4,2*10**-4,200,100]

D = {"Title":Title,"Value":Value}

Datas = pd.DataFrame(D)
'''
print(Datas)

Datas.to_csv("Parameters.csv",index=True)
