import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import join
import functions as f

#Set plot style
plt.rcParams.update({'font.size': 15})
fig, ax = plt.subplots(figsize=(8,6))
plt.xlim([0.05,15])
AC1 = ax.vlines(x=0.3, ymin=0, ymax=10, colors=(0.8,0.8,0.8), linestyle='solid')
AC2 = ax.vlines(x=0.1, ymin=0, ymax=10, colors=(0.8,0.8,0.8), linestyle='solid')
dash = '--'
line = '-'
color = ['r',(0.8,0.52,0),(0.8,0.8,0),(0,0.8,0),'b',(111/255, 0, 255/255),(238/255,130/255,238/255),'k']

#Load Datas
print("Please input the desired directory:")
path = input()
Datas = f.Import_Datas(path)

#Plotting function
def Plot_SED_Components(Datas, i):
    #Datas[Datas==0] = 1e-60
    #ROW = f.Find_Lambda_ROW(0.3,Datas)
    Data = Datas[i]
    ax.loglog(Data[:,0], Data[:,1], color='b', linestyle='solid', label='Total Flux')
    ax.loglog(Data[:,0], Data[:,2], color='b', linestyle='dashed', label='Intrinsic Flux')
    ax.loglog(Data[:,0], Data[:,3], color='b', linestyle=':', label='Direct Primary Flux')
    ax.loglog(Data[:,0], Data[:,4], color='c', linestyle=':', label='Scattered Primary Flux')
    plt.ylim([1e-4,1e2])
    plt.legend()
    plt.show()

def Ratio_DS(Datas, i):
    Data = Datas[i]
    plt.loglog(Data[:,0], Data[:,3]/Data[:,4], label='Direct/Scattered')
    plt.legend()
    plt.show()

Ratio_DS(Datas, -1)
#Plot_SED_Components(Datas, -1)
