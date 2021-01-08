import functions as f
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 20})
fig, ax = plt.subplots(figsize=(8,6))

path = input("Please input the desired directory:")

Datas = f.Import_Datas(path)

for i in Datas:



plt.show()
