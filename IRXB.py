import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from os import listdir
from os.path import join
import pandas as pd

#Set plotting style
plt.rcParams.update({'font.size': 20})
fig, ax = plt.subplots(figsize=(8,6))

#Parameters
c = 299792458
Beta_range = [0.15,0.3]

#Load SEDs
print("Please input the desired directory:")
path = input()
files = listdir(path)
files_abs = files
files_abs.sort() #Sort the files to order them by radius
R = [] #Record the radius of each simulation
for i in range(len(files)):
    files_abs[i] = join(path,files[i])
    R.append(files_abs[i].split('/')[-1].split('.')[-2].split('=')[-1])
R = np.asarray(list(map(int, R)))/1000
print(R)

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

def Cal_Beta(Datas, Range):
    TotalFlux = Datas[:,1]
    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0] > Range[0]:
             Row1600A = rows
             break

    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0] > Range[1]:
             Row2500A = rows
             break

    Beta = np.log10(TotalFlux[Row1600A]/TotalFlux[Row2500A])/np.log10(1600/2500)-2
    return Beta

#Main code
for i in range(0,len(files_abs)):
    Datas = np.loadtxt(files_abs[i])
    
    #Calculate IRX and Beta
    IRX = Cal_IRX(Datas)
    Beta = Cal_Beta(Datas, Beta_range)
    print(Beta)

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
#CBMax = 5
#CBMin = 1
#color = np.linspace(CBMin,CBMax,int(len(files)/2))

#IRXB Curve
x = np.linspace(-5,1,100)
Calzetti = np.log10(10**(0.4*(4.43+1.99*x))-1)+0.076
SMC = np.loadtxt('./Observation_Datas/irx.dat')
ax.plot(x,Calzetti,'k-',label='Calzetti')
ax.plot(SMC[:,0],np.log10(SMC[:,1]),'k--',label='SMC')

#Plot simulation data points
DG = plt.scatter(x = Data[:int(len(files)/2),0], y = Data[:int(len(files)/2),1], s = 100, c = R[:int(len(files)/2)], marker = 'o', zorder = 10, cmap = 'gist_rainbow')
SD = plt.scatter(x = Data[int(len(files)/2):,0], y = Data[int(len(files)/2):,1], s = 100, c = R[int(len(files)/2):], marker = '^', zorder = 10, cmap = 'gist_rainbow')

#Draw colorbar
CBar = plt.colorbar()
CBar.ax.set_title('kpc')
#plt.clim(R[0] - (R[0] + R[-1])/10, R[-1] + (R[0] + R[-1])/10)
plt.clim(0.5,5.5)

#Legend
plt.scatter(-10,-10, color='k', marker='^',label='Star dust scenario')
plt.scatter(-10,-10, color='k', marker='o',label='Dust growth scenario')

#Plot setting
plt.legend(loc=4,prop={'size': 15})
plt.xlim([-3,1])
plt.ylim([-2,3])
plt.xlabel(r'$\beta$ (UV slope)')
plt.ylabel(r'$IRX=log(L_{IR}/L_{UV})$')
plt.tight_layout()
plt.savefig('{}_IRXB_SameS'.format(path),dpi=300)
plt.show()
