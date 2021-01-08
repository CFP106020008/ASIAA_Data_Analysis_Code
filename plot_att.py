import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import join
import functions as f

#Set plot style
plt.rcParams.update({'font.size': 20})
fig, ax = plt.subplots(figsize=(8,6))
dash = '--'
line = '-'
color = ['r',(0.8,0.52,0),(0.8,0.8,0),(0,0.8,0),'b',(111/255, 0, 255/255),(238/255,130/255,238/255),'k']

#Load Datas
print("Please input the desired directory:")
path = input()
Datas = f.Import_Datas(path)

#Main code to plot
for i in range(0,len(files_abs)):
    Plot_AttCur(Datas[i],i)
    if i<len(files_abs)/2:
#f.Plot_AttCur_Fill(Datas[:int(len(Datas)/2)],'b','dashed',LABEL="Dust growth scenario")
#f.Plot_AttCur_Fill(Datas[int(len(Datas)/2):],'r','solid' ,LABEL="Star dust scenario")

#Plot legends
#StarDust = ax.plot(np.linspace(0,10,10), np.ones(10)*-1, color = (0.1,0.1,0.1), linestyle='solid', label='Star dust scenario', linewidth=3)
#DustGrowth = ax.plot(np.linspace(0,10,10), np.ones(10)*-1, color = (0.1,0.1,0.1), linestyle='dashed', label='Dust growth scenario', linewidth=3)
f.Plot_Ext()

#Show SMC and Calzetti curves
SMC = np.loadtxt('./Observation_Datas/pei_smc.dat')
Calzetti = np.loadtxt('./Observation_Datas/calzetti.dat')
Line_SMC = ax.plot(SMC[:,0], SMC[:,2]/1.9, color = (0.5,0.5,0.5), linestyle=':', label='SMC extinction curve', linewidth=3)
Line_Cal = ax.plot(1/Calzetti[:,0], Calzetti[:,1], color = (0.3,0.3,0.3), linestyle=':', label='Calzetti attenuation curve', linewidth=3)

#Show the beta wavelengths
B_short = ax.vlines(x=1/0.16, ymin=0, ymax=10, colors=(0.8,0.8,0.8), linestyle='solid')
B_long = ax.vlines(x=1/0.25, ymin=0, ymax=10, colors=(0.8,0.8,0.8), linestyle='solid')

handles, labels = plt.gca().get_legend_handles_labels()
order = [4,5,2,3,0,1]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc=2,prop={'size': 15})


#Set plot style
#plt.legend(loc=2,prop={'size': 15})
#plt.title("Attenuation Curve \n (Normalized at {:4f} $\mu m$)".format(Datas[ROW,0]))
plt.xlabel(r'$1/\lambda$ $(\mu m^{-1})$')
plt.ylabel(r'$A/A_{3000 \AA}$')
plt.xlim([0.3,10])
plt.ylim([0,10])
plt.tight_layout()
plt.savefig(str(path+"_Attcur.png"),dpi=300)
#plt.show()
print('OK!')
