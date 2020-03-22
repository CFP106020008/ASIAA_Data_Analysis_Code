import numpy as np
import matplotlib.pyplot as plt

print("input file name:")
Datas = np.loadtxt(input())
plt.style.use('dark_background')

plt.loglog(Datas[:,0],Datas[:,1],'-w', label = "Total")
plt.loglog(Datas[:,0],Datas[:,2],':b',label = "Transparent")
plt.loglog(Datas[:,0],Datas[:,3] + Datas[:,4],'--y',label = "Primary")
plt.loglog(Datas[:,0],Datas[:,5] + Datas[:,6],'--r',label = "Secondary")
plt.legend()
plt.xlabel("Wavelength (micrometer)")
plt.ylabel("Flux (Jy)")
plt.xlim([10**-1,10**3])
plt.ylim([10**-3,10**4])
plt.show()




