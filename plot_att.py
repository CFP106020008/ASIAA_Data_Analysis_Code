import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import join

#Set plot style
plt.rcParams.update({'font.size': 20})
fig, ax = plt.subplots(figsize=(8,6))
dash = '--'
line = '-'
#color = np.linspace(1000,5000,int(len(files)/2))
color = ['r',(0.8,0.52,0),(0.8,0.8,0),(0,0.8,0),'b',(111/255, 0, 255/255),(238/255,130/255,238/255),'k']
#color = [(0.5,0.5,0.5),(0.6,0.5,0.5),(0.7,0.5,0.5),(0.8,0.5,0.5),(0.9,0.5,0.5),(1,0.5,0.5)]


#Load Datas
print("Please input the desired directory:")
path = input()
files = listdir(path)
files.sort()
files_abs = files
files_abs.sort()
for i in range(len(files)):
    files_abs[i] = join(path,files[i])

#Show datas
for i in range(0,len(files_abs)):
    Datas = np.loadtxt(files_abs[i])
    Datas[Datas==0] = 1e-60
    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0]>0.3:
            ROW = rows
            break
    tau = (np.log(Datas[:,2]/Datas[:,1]))/(np.log(Datas[ROW,2]/Datas[ROW,1]))
    #print(tau[1])
    LABEL = files[i].split('/')[-1]
    
    if i<0.5*len(files_abs):
        ax.plot(1/Datas[:,0],tau,color=color[i],linestyle='dashed')#,label=LABEL)
    else:
        ax.plot(1/Datas[:,0],tau,color=color[int(i-0.5*len(files_abs))],linestyle='solid')#,label=LABEL)

#Plot for legends
StarDust = ax.plot(np.linspace(0,10,10), np.ones(10)*-1, color = (0.1,0.1,0.1), linestyle='solid', label='Star dust scenario', linewidth=3)
DustGrowth = ax.plot(np.linspace(0,10,10), np.ones(10)*-1, color = (0.1,0.1,0.1), linestyle='dashed', label='Dust growth scenario', linewidth=3)

#Show SMC and Calzetti curves
SMC = np.loadtxt('./Observation_Datas/pei_smc.dat')
Calzetti = np.loadtxt('./Observation_Datas/calzetti.dat')
Line_SMC = ax.plot(SMC[:,0], SMC[:,2]/1.9, color = (0.5,0.5,0.5), linestyle=':', label='SMC', linewidth=3)
Line_Cal = ax.plot(1/Calzetti[:,0], Calzetti[:,1], color = (0.3,0.3,0.3), linestyle=':', label='Calzetti', linewidth=3)

#Show the beta wavelengths
B_short = ax.vlines(x=1/0.16, ymin=0, ymax=10, colors=(0.8,0.8,0.8), linestyle='solid')
B_long = ax.vlines(x=1/0.25, ymin=0, ymax=10, colors=(0.8,0.8,0.8), linestyle='solid')

#Set plot style
plt.legend(loc=2,prop={'size': 15})
#plt.title("Attenuation Curve \n (Normalized at {:4f} $\mu m$)".format(Datas[ROW,0]))
plt.xlabel(r'$1/\lambda$ $(\mu m^{-1})$')
plt.ylabel(r'$A/A_{3000 \AA}$')
plt.xlim([0.3,10])
plt.ylim([0,10])
plt.tight_layout()
plt.savefig(str(path+"_Attcur.png"),dpi=300)
#plt.show()
