import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import join
'''
path = "./Ages" 
files = listdir(path) 
files_abs = files 
for i in range(len(files)):
    files_abs[i] = join(path,files[i])

for i in files_abs:
    Datas = np.loadtxt(i)
    plt.loglog(Datas[:,0],Datas[:,1], label = i)
'''
Datas = np.loadtxt("DustDistribution.dat")
plt.loglog(Datas[:,0],Datas[:,1]) #label = i)
plt.legend()
plt.xlabel("a (cm)")
plt.ylabel("Dust to gas ratio")
#plt.xlim([10**-2,10**4])
plt.ylim([10**-6,10**-1])

plt.show()

