import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import join

path = "./Ages"
files = listdir(path)
files_abs = files
for i in range(len(files)):
    files_abs[i] = join(path,files[i])

style_list = ['r-','y-','b-','r--','y--','b--','r:','y:','b:']

for i in range(0,len(files_abs)):
    Data = np.loadtxt(files_abs[i])
    plt.loglog(Data[:,0],Data[:,1],style_list[i],label=files_abs[i])

plt.legend()
plt.show()
