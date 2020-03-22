import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import join

c=299792458
path = input() 
files = listdir(path) 
files_abs = files 
for i in range(len(files)):
    files_abs[i] = join(path,files[i])

for i in files_abs:
    Datas = np.loadtxt(i)
    plt.loglog(Datas[:,0],Datas[:,1]*c/Datas[:,0], label = i)

plt.legend()
plt.xlabel("Wavelength (micrometer)")
plt.ylabel("Flux*frequency (Jy*Hz)")
plt.xlim([10**-1,10**3])
plt.ylim([10**5,10**12])

plt.show()
