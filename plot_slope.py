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
for i in range(len(files)):
    files_abs[i] = join(path,files[i])

#Show datas
for i in range(0,len(files_abs)):
    Datas = np.loadtxt(files_abs[i])
    Datas[Datas==0] = 1e-60
    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0]>0.3:
            ROW3000 = rows
            break
    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0]>0.15:
            ROW1500 = rows
            break
    #UV slope
    slope = np.log(Datas[ROW1500,2]/Datas[ROW1500,1])/np.log(Datas[ROW3000,2]/Datas[ROW3000,1])
    #print(slope)
    LABEL = files[i].split('/')[-1]
    
    if i<0.5*len(files_abs):
        ax.scatter((i+1)*1000,slope,color=color[i],marker='o')#,label=LABEL)
    else:
        ax.scatter(int((i+1)-0.5*len(files_abs))*1000,slope,color=color[int(i-0.5*len(files_abs))],marker='^')#,label=LABEL)

#Legend
plt.scatter(-10,-10, color='k', marker='^',label='Star dust scenario')
plt.scatter(-10,-10, color='k', marker='o',label='Dust growth scenario')

#Set plot style
plt.legend(loc=2)
#plt.title("Attenuation Curve \n (Normalized at {:4f} $\mu m$)".format(Datas[ROW,0]))
plt.xlabel(r'R (pc)')
plt.ylabel(r'UV slope ($A_{1500}/A_{3000}$)')
plt.xlim([900,5100])
plt.ylim([1,8])
plt.tight_layout()
plt.savefig(str(path+"_slope.png"),dpi=300)
