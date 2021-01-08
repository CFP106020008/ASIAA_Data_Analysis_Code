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
Datas = np.loadtxt(path)

def Find_Lambda_ROW(Wavelength,Datas):
    W = np.ones((np.shape(Datas)[0],1))*Wavelength
    ROW = (np.abs(Datas[:,0] - W)).argmin()
    return ROW

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

#Main code to plot
plt.plot(Datas[:,0],Datas[:,1], label="total", color='k',linestyle='solid') 
plt.plot(Datas[:,0],Datas[:,2], label="intrinsic", color='b',linestyle='solid') 
plt.plot(Datas[:,0],Datas[:,3], label="primary direct", color='b',linestyle='dashed') 
plt.plot(Datas[:,0],Datas[:,4], label="primary scattered", color='r',linestyle='dashed') 

#Show the beta wavelengths
B_short = ax.vlines(x=0.16, ymin=0, ymax=10, colors=(0.8,0.8,0.8), linestyle='solid')
B_long = ax.vlines(x=0.25, ymin=0, ymax=10, colors=(0.8,0.8,0.8), linestyle='solid')

#handles, labels = plt.gca().get_legend_handles_labels()
#order = [4,5,2,3,0,1]
#plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc=2,prop={'size': 15})
plt.legend()

#Set plot style
#plt.legend(loc=2,prop={'size': 15})
#plt.title("Attenuation Curve \n (Normalized at {:4f} $\mu m$)".format(Datas[ROW,0]))
plt.xlabel(r'$1/\lambda$ $(\mu m^{-1})$')
plt.ylabel(r'$A/A_{3000 \AA}$')
plt.xlim([1e-1,1e3])
plt.ylim([1e-3,1e3])
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
plt.savefig(str(path+"_SED.png"),dpi=300)
#plt.show()
print('OK!')
