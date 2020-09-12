import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import join

#Set plot style
plt.rcParams.update({'font.size': 20})
fig, ax = plt.subplots(figsize=(8,6))
dash = '--'
line = '-'
color = ['r',(0.8,0.52,0),(0.8,0.8,0),(0,0.8,0),'b',(111/255, 0, 255/255),(238/255,130/255,238/255),'k']

#Load Datas
print("Please input the desired directory:")
path = input()
files = listdir(path)
files.sort()
files_abs = files
files_abs.sort()
Datas = []
for i in range(len(files)):
    files_abs[i] = join(path,files[i])
    Datas.append(np.loadtxt(files_abs[i]))

#Plotting function
def Plot_AttCur(Datas,i):
    Datas[Datas==0] = 1e-60
    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0]>0.3:
            ROW = rows
            break
    tau = (np.log(Datas[:,2]/Datas[:,1]))/(np.log(Datas[ROW,2]/Datas[ROW,1]))
    if i<0.5*len(files_abs):
        ax.plot(1/Datas[:,0],tau,color=color[i],linestyle='dashed')
    else:
        ax.plot(1/Datas[:,0],tau,color=color[int(i-0.5*len(files_abs))],linestyle='solid')   

#Plot with fill_in
def Plot_AttCur_Fill(Datas,COLOR,LINE,LABEL):
    tau = []
    Wavelength = Datas[0][:,0]
    for rows in range(0,np.shape(Wavelength)[0]):
        if Wavelength[rows]>0.3:
            ROW = rows
            break
    for D in Datas:
        tau.append((np.log(D[:,2]/D[:,1]))/(np.log(D[ROW,2]/D[ROW,1])))
    plt.fill_between(1/Wavelength,tau[0],tau[-1],alpha=0.3,color=COLOR,linestyle=LINE,label=LABEL)

#Main code to plot
#for i in range(0,len(files_abs)):
    #Plot_AttCur(Datas[i],i)
    #if i<len(files_abs)/2:
Plot_AttCur_Fill(Datas[:int(len(Datas)/2)],'b','dashed',LABEL="Dust growth scenario")
Plot_AttCur_Fill(Datas[int(len(Datas)/2):],'r','solid' ,LABEL="Star dust scenario")

#Plot legends
#StarDust = ax.plot(np.linspace(0,10,10), np.ones(10)*-1, color = (0.1,0.1,0.1), linestyle='solid', label='Star dust scenario', linewidth=3)
#DustGrowth = ax.plot(np.linspace(0,10,10), np.ones(10)*-1, color = (0.1,0.1,0.1), linestyle='dashed', label='Dust growth scenario', linewidth=3)

#Show extinction curves of the two scenarios
Ext_SD = np.loadtxt('./Observation_Datas/Extinction_Curve/ext_yenhsing_stellar.dat')
Ext_DG = np.loadtxt('./Observation_Datas/Extinction_Curve/ext_yenhsing_accretion.dat')
for rows in range(np.shape(Ext_DG)[0]):
    if Ext_DG[rows,0]<0.3:
        ROW = rows
        break
plt.plot(1/Ext_DG[:,0],Ext_DG[:,3]/Ext_DG[ROW,3],color='r',linestyle='dashed',label="Ext. curve of D.G. scenario")
plt.plot(1/Ext_SD[:,0],Ext_SD[:,3]/Ext_SD[ROW,3],color='r',linestyle='solid',label="Ext. curve of S.D. scenario")

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
