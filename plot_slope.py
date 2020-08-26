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
        ax.scatter(i*1000,tau[1],color=color[i],linestyle='dashed')#,label=LABEL)
    else:
        ax.plot(int(i-0.5*len(files_abs))*1000,tau[1],color=color[int(i-0.5*len(files_abs))],linestyle='solid')#,label=LABEL)

#Set plot style
plt.legend(loc=2)
#plt.title("Attenuation Curve \n (Normalized at {:4f} $\mu m$)".format(Datas[ROW,0]))
plt.xlabel(r'R')
plt.ylabel(r'slope')
#plt.xlim([0.3,10])
#plt.ylim([0,10])
plt.tight_layout()
plt.savefig(str(path+"_slope.png"),dpi=300)
