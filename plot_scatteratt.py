import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import join

print("Please input the desired directory:")
path = input()
files = listdir(path)
files.sort()
files_abs = files
files_abs.sort()
for i in range(len(files)):
    files_abs[i] = join(path,files[i])

dash = '--'
line = '-'
color = ['r','y','g','b','c','k','m']

for i in range(0,len(files_abs)):
    Datas = np.loadtxt(files_abs[i])
    Datas[Datas==0] = 1e-20
    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0]>0.3:
            ROW = rows
            break
    #print(Datas[ROW,0])
    tau = (np.log(Datas[:,1]/Datas[:,4]))#/(np.log(Datas[ROW,4]/Datas[ROW,1]))
    if i<0.5*len(files_abs):
        plt.plot(1/Datas[:,0],tau,color[i]+dash,label=files[i])
    else:
        plt.plot(1/Datas[:,0],tau,color[int(i-0.5*len(files_abs))]+line,label=files[i])

plt.legend()
#plt.title("Attenuation Curve \n (Normalize to {} $\mu m$)".format(Datas[ROW,0]))
plt.xlabel(r'$1/\lambda$ $(\mu m^{-1})$')
plt.ylabel(r'$A(\lambda)$')
plt.xlim([0.3,1/0.09])
plt.ylim([0,10])
plt.savefig(str(path+"scattered_Attcur.png"),dpi=300)
plt.show()
