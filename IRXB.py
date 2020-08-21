import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from os import listdir
from os.path import join
import pandas as pd

#Set plotting style
plt.rcParams.update({'font.size': 20})
fig, ax = plt.subplots(figsize=(8,6))
color = ['r',(0.8,0.52,0),(0.8,0.8,0),(0,0.8,0),'b']#,(111/255,0,255/255),(238/255,130/255,238/255)]
cMap = ListedColormap(color)

#Light Speed
c = 299792458

#Load SEDs
print("Please input the desired directory:")
path = input()
files = listdir(path)
files_abs = files
files_abs.sort()
for i in range(len(files)):
    files_abs[i] = join(path,files[i])

#create a matrix to store beta and irx
Data = np.zeros((len(files),2))

def Cal_IRX(Datas):
    nu = c/(Datas[:,0]*10**-6)
    TotalFlux = Datas[:,1]
    nu3 = c/(3*10**-6)
    nu1000 = c/(1000*10**-6)
    for rows in range(0,np.shape(Datas)[0]):
        if nu[rows]<nu3:
             Row3 = rows
             break
    for rows in range(0,np.shape(Datas)[0]):
        if nu[rows]<nu1000:
             Row1000 = rows
             break
    LIR = -np.trapz(TotalFlux[Row3:Row1000],x=nu[Row3:Row1000])

    #UV Part
    nu1600A = 299792458/(1600*10**-10)

    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0]>0.16:
             Row1600 = rows
             break
    UV = TotalFlux[Row1600]*nu[Row1600]
    IRX = LIR/UV
    return IRX

def Cal_Beta(Datas):
    TotalFlux = Datas[:,1]
    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0]>0.16:
             Row1600A = rows
             break

    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0]>0.25:
             Row2500A = rows
             break

    Beta = np.log10(TotalFlux[Row1600A]/TotalFlux[Row2500A])/np.log10(1600/2500)-2
    return Beta

#Main code
for i in range(0,len(files_abs)):
    Datas = np.loadtxt(files_abs[i])
    
    #Calculate IRX and Beta
    IRX = Cal_IRX(Datas)
    Beta = Cal_Beta(Datas)

    #Plot data points
    LABEL = files[i].split('/')[-1]
    Data[i,:] = np.array([Beta,np.log10(IRX)])

#Observation Datas
Obs = pd.read_csv("./Observation_Datas/Observations_good.csv",index_col=0)
IRXs = Obs.loc[:,'IRX'].to_numpy().transpose()
Betas = Obs.loc[:,'beta'].to_numpy().transpose()
IRX_err = Obs.loc[:,'IRX_error+':'IRX_error-'].to_numpy().transpose()
Beta_err = Obs.loc[:,'beta_error+':'beta_error-'].to_numpy().transpose()
Beta_LL = Obs.loc[:,'beta_lowlim'].to_numpy().transpose()
Beta_UL = Obs.loc[:,'beta_uplim'].to_numpy().transpose()
IRX_LL = Obs.loc[:,'IRX_lowlim'].to_numpy().transpose()
IRX_UL = Obs.loc[:,'IRX_uplim'].to_numpy().transpose()
plt.errorbar(   x = Betas,
                y = IRXs,
                xerr = Beta_err,
                yerr = IRX_err,
                xlolims = Beta_LL,
                xuplims = Beta_UL,
                lolims = IRX_LL,
                uplims = IRX_UL,
                fmt='s',
                ecolor='gray',
                mfc='gray',
                mec='gray',)
                #zorder=5.) 

#Set colorbar style
CBMax = 5
CBMin = 1
color = np.linspace(CBMin,CBMax,int(len(files)/2))

#IRXB Curve
x = np.linspace(-5,1,100)
Calzetti = np.log10(10**(0.4*(4.43+1.99*x))-1)+0.076
SMC = np.loadtxt('./Observation_Datas/irx.dat')
ax.plot(x,Calzetti,'k-',label='Calzetti')
ax.plot(SMC[:,0],np.log10(SMC[:,1]),'k--',label='SMC')

#Plot simulation data points
plt.scatter(x = Data[:int(len(files)/2),0], y = Data[:int(len(files)/2),1], s = 100, cmap = cMap, c = color, marker = 'o', zorder=10)
plt.scatter(x = Data[int(len(files)/2):,0], y = Data[int(len(files)/2):,1], cmap = cMap, s = 100, c = color, marker = '^',zorder=10)

#Draw colorbar
CBar = plt.colorbar(ticks = np.linspace(CBMin,CBMax,int(len(files)/2)))
CBar.ax.set_title('kpc')
plt.clim(CBMin-(CBMax-CBMin)/int(len(files)/2-1)/2,CBMax+(CBMax-CBMin)/int(len(files)/2-1)/2)

plt.legend(loc=4)
plt.xlim([-3,1])
plt.ylim([-2,3])
plt.xlabel(r'$\beta$')
plt.ylabel(r'$IRX$')
plt.tight_layout()
plt.savefig('{}_IRXB'.format(path),dpi=300)
plt.show()
