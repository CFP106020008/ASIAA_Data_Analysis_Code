import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import join
import pandas as pd

'''Load SEDs'''
print("Please input the desired directory:")
path = input()
files = listdir(path)
files_abs = files
files_abs.sort()
for i in range(len(files)):
    files_abs[i] = join(path,files[i])

'''Ploting Parameter'''
s = np.array([1,2,3,4,5,6,7])*5

L = ['Contrast=1','Contrast=25','Contrast=50','Contrast=75','Contrast=100','Contrast=125','Contrast=150']
for i in range(0,len(files_abs)):
    Datas = np.loadtxt(files_abs[i])
    print(files_abs[i])
    '''LIR Part'''
    nu = 299792458/(Datas[:,0]*10**-6)
    TotalFlux = Datas[:,1]
    nu3 = 299792458/(3*10**-6)
    #print('nu3 = {}'.format(nu3))
    nu1000 = 299792458/(1000*10**-6)
    #print('nu1000 = {}'.format(nu1000))
    for rows in range(0,np.shape(Datas)[0]):
        if nu[rows]<nu3:
             Row3 = rows
             break
    #print(Datas[Row3,0])
    for rows in range(0,np.shape(Datas)[0]):
        if nu[rows]<nu1000:
             Row1000 = rows
             break
    #print(Datas[Row1000,0])
    #plt.loglog(nu[Row3:Row1000],TotalFlux[Row3:Row1000])
    #plt.show()
    LIR = -np.trapz(TotalFlux[Row3:Row1000],x=nu[Row3:Row1000])
    #print(LIR)

    '''UV Part'''
    nu1600A = 299792458/(1600*10**-10)

    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0]>0.16:
             Row1600 = rows
             break
    UV = TotalFlux[Row1600]*nu[Row1600]
    #print(UV)
    IRX = LIR/UV

    #print('log(IRX) = {}'.format(np.log10(IRX)))

    '''Beta Part'''
    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0]>0.16:
             Row1600A = rows
             break

    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0]>0.25:
             Row2500A = rows
             break

    Beta = np.log10(TotalFlux[Row1600A]/TotalFlux[Row2500A])/np.log10(1600/2500)-2
    #print("Beta = {}".format(Beta))
    
    if i< 0.5*len(files_abs):
        plt.scatter(Beta,np.log10(IRX),marker='o',label=str('Accretion: '+L[i]))
    else:
        plt.scatter(Beta,np.log10(IRX),marker='^',label=str('Stellar: '+L[int(i-0.5*len(files_abs))]))
    '''
    if i< 0.5*len(files_abs):
        plt.scatter(Beta,np.log10(IRX),marker='o',s=s[i])#,label=files_abs[i])
    else:
        plt.scatter(Beta,np.log10(IRX),marker='^',s=s[int(i-0.5*len(files_abs))])#,label=files_abs[i])
    '''
    
'''
#Observation Datas
Obs = pd.read_csv("./Observation_Datas/Observations_good.csv",index_col=0)

IRXs = Obs.loc[:,'IRX'].to_numpy().transpose()
#IRXs = Obs.loc[:,'IRX'].tolist()

Betas = Obs.loc[:,'beta'].to_numpy().transpose()
#Betas = Obs.loc[:,'beta'].tolist()

#IRX_err = Obs.loc[:,'IRX_error+':'IRX_error-'].to_numpy().transpose()
IRX_err = Obs.loc[:,'IRX_error+':'IRX_error-'].values

#Beta_err = Obs.loc[:,'beta_error+':'beta_error-'].to_numpy().transpose()
Beta_err = Obs.loc[:,'beta_error+':'beta_error-'].values

#plt.errorbar(Betas,IRXs,xerr=Beta_err,yerr=IRX_err,fmt='*') 
plt.errorbar(Obs.beta,Obs.IRX,xerr=Obs.loc[:,'beta_error+':'beta_error-'],yerr=Obs.loc[:,'IRX_error+':'IRX_error-'],xuplims=Obs.beta_uplim,fmt='*')
'''

'''IRXB Curve'''
x = np.linspace(-5,1,100)
Calzetti = np.log10(10**(0.4*(4.43+1.99*x))-1)+0.076
SMC = np.loadtxt('./Observation_Datas/irx.dat')
plt.plot(x,Calzetti,'k-',label='Calzetti')
plt.plot(SMC[:,0],np.log10(SMC[:,1]),'k--',label='SMC')

'''Fiducial Cases'''
plt.legend()
plt.xlim([-3,1])
plt.ylim([-2,3])
plt.title(r'IRX-$\beta$',fontsize=20)
plt.xlabel(r'$\beta$',fontsize=15)
plt.ylabel(r'$IRX=log \frac{L_{IR}}{L_{UV1600}}$',fontsize=15)
plt.savefig('{}_IRXB'.format(path))
#plt.show()
