import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import join

Ext_SD = np.loadtxt('./Observation_Datas/Extinction_Curve/ext_yenhsing_stellar.dat')
Ext_DG = np.loadtxt('./Observation_Datas/Extinction_Curve/ext_yenhsing_accretion.dat')

def Find_Lambda_ROW(Wavelength,Datas):
    W = np.ones((np.shape(Datas)[0],1))*Wavelength
    ROW = (np.abs(Datas[:,0] - W)).argmin()
    return ROW

def dB_max(Data, L1, L2):
    ROW1 = Find_Lambda_ROW(L1,Data)
    ROW2 = Find_Lambda_ROW(L2,Data)
    dbeta = -np.log(Data[ROW1,3]/Data[ROW2,3])/np.log(L1/L2)
    return dbeta

def tau_eff(tau):
    taueff = -np.log((3/(4*tau)(1-1/(2*tau**2)+(1/tau+1/(2*tau**2)*np.exp(-2*tau)))))
    return taueff

def dB(Ext_Cuv,L1,L2,SF):
    ROW1 = Find_Lambda_ROW(L1,Data)
    ROW2 = Find_Lambda_ROW(L2,Data)
    teff1 = tau_eff(np.log(Ext_Cuv[ROW1,3]*SF))
    teff2 = tau_eff(np.log(Ext_Cuv[ROW2,3]*SF))
    dB = -(teff2-teff1)/(np.log(L2/L1))
    return dB
    
x = np.linspace(1,1e5)

plt.plot(SD[:,0], SD[:,1], color='r', linestyle='solid',label='')




#print('db-SD:',dB_max(Ext_SD,0.16,0.25))
#print('db-DG:',dB_max(Ext_DG,0.16,0.25))





