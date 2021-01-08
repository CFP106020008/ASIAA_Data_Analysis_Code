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

def Find_Lambda_ROW(Wavelength,Datas):
    W = np.ones((np.shape(Datas)[0],1))*Wavelength
    ROW = (np.abs(Datas[:,0] - W)).argmin()
    return ROW

slope = [] #Record UV slopes
AV = [] #Record A_V
R = [] #Record the radius of each simulation
for i in range(len(files)):
    R.append(files_abs[i].split('/')[-1].split('.')[-2].split('=')[-1])
R = np.asarray(list(map(int, R)))/1000

#Show datas
for i in range(0,len(files_abs)):
    Datas = np.loadtxt(files_abs[i])
    Datas[Datas==0] = 1e-60
    ROW3000 = Find_Lambda_ROW(0.3,Datas)
    ROW1500 = Find_Lambda_ROW(0.15,Datas)
    ROW5500 = Find_Lambda_ROW(0.55,Datas)
    
    #UV slope
    slope.append(np.log(Datas[ROW1500,2]/Datas[ROW1500,1])/np.log(Datas[ROW3000,2]/Datas[ROW3000,1]))
    AV.append(np.log(Datas[ROW5500,2]/Datas[ROW5500,1]))

DG = plt.scatter(x = AV[:int(len(files)/2)], y = slope[:int(len(files)/2)], s = 100, c = R[:int(len(files)/2)], marker = 'o', zorder = 10, cmap = 'gist_rainbow')
SD = plt.scatter(x = AV[int(len(files)/2):], y = slope[int(len(files)/2):], s = 100, c = R[int(len(files)/2):], marker = '^', zorder = 10, cmap = 'gist_rainbow')
CB = plt.colorbar(DG)    
CB.ax.set_title('kpc')
plt.clim(0.5,5.5)

print(R[:int(len(files)/2)])
print(R[int(len(files)/2):])


#Legend
plt.scatter(-10,-10, color='k', marker='^',label='Star dust scenario')
plt.scatter(-10,-10, color='k', marker='o',label='Dust growth scenario')

#Original extinction curves
Ext_SD = np.loadtxt('./Observation_Datas/Extinction_Curve/ext_yenhsing_stellar.dat')
Ext_DG = np.loadtxt('./Observation_Datas/Extinction_Curve/ext_yenhsing_accretion.dat')
ROW1500 = Find_Lambda_ROW(0.15,Ext_SD)
ROW3000 = Find_Lambda_ROW(0.30 ,Ext_SD)
ROW5500 = Find_Lambda_ROW(0.55 ,Ext_SD)

slope_SD = Ext_SD[ROW1500,3]/Ext_SD[ROW3000,3]
slope_DG = Ext_DG[ROW1500,3]/Ext_DG[ROW3000,3]
plt.hlines(y=slope_SD, xmin=-10, xmax=10, colors='k', linestyles='solid' , alpha=0.2, label='Slope of S.D. scenario')
plt.hlines(y=slope_DG, xmin=-10, xmax=10, colors='k', linestyles='dashed', alpha=0.2, label='Slope of D.G. scenario')

#Set plot style
plt.legend(loc=1,prop={'size': 15})
#plt.title("Attenuation Curve \n (Normalized at {:4f} $\mu m$)".format(Datas[ROW,0]))
plt.xlabel(r'$A_{V}$')
plt.ylabel(r'$A_{1500}/A_{3000}$')
#===This is for TL===#
plt.xlim([0.005,0.04])
plt.ylim([0,15])
#===This is for WM===#
#plt.xlim([-0.1,1.5])
#plt.ylim([0,10])

plt.tight_layout()
plt.savefig(str(path+"_slope3000.png"),dpi=300)
