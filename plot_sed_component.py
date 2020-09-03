import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import join

#light speed
c = 299792458e6

#Set plot style
plt.rcParams.update({'font.size': 20})
fig, ax = plt.subplots(figsize=(8,6))
color = ['r',(0.8,0.52,0),(0.8,0.8,0),(0,0.8,0),'b',(111/255, 0, 255/255),(238/255,130/255,238/255),'k']


#Load Datas
print("Please input the desired directory:")
path = input()

Datas = np.loadtxt(path)
Datas[Datas==0] = 1e-60
for rows in range(0,np.shape(Datas)[0]):
    if Datas[rows,0]>0.3:
        ROW = rows
        break
Wavelen = Datas[:,0]
intensity = Datas[:,1]
intrinsic = Datas[:,2]
Name = path.split('.')[0]

ax.loglog(Wavelen, intensity, color='k', lw=4, linestyle='solid',label='Extincted')
ax.loglog(Wavelen, intrinsic, color='b', lw=4, linestyle='dashed',label='Intrinsic')


#Show the beta wavelengths
#B_short = ax.vlines(x=0.16, ymin=0, ymax=1e20, colors=(0.8,0.8,0.8), linestyle='solid')
#B_long = ax.vlines(x=0.25, ymin=0, ymax=1e20, colors=(0.8,0.8,0.8), linestyle='solid')

#Set plot style
plt.legend(loc=2)
plt.xlabel("Wavelength (micrometer)")
plt.ylabel("Intensity (Jy)")
plt.xlim([10**-1,10**3])
plt.ylim([np.min(intensity/10),np.max(intensity*10)])
plt.tight_layout()
plt.savefig(str(Name+"_SED.png"),dpi=300)
#plt.show()
