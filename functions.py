import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from os import listdir
from os.path import join

#Plot indivisual attenuation curves
def Plot_AttCur(Datas,i,color):
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

#Plot with fill_in
def Plot_AttCur_Fill(Datas,COLOR,LINE,LABEL):
    tau = []
    Wavelength = Datas[0][:,0]
    for rows in range(0,np.shape(Wavelength)[0]):
        if Wavelength[rows]>0.3:
            ROW = rows
            break
    for D in Datas:
        tau.append((np.log(D[:,2]/D[:,1]))/(np.log(D[ROW,2]/D[ROW,1])))
    plt.fill_between(1/Wavelength,tau[0],tau[-1],alpha=0.3,color=COLOR,linestyle=LINE,label=LABEL)

#Find the row corresponds to particular wavelength
def Find_Lambda_ROW(Wavelength,Datas):
    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0]>Wavelength:
            ROW = rows
            break
    return ROW

#Calculate IRX
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

#Calculate beta
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

#Plot IRXB observation datas from Hashimoto et al. (2019)
def Plot_IRXB_Obs():
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

def Plot_Ext():
    Ext_SD = np.loadtxt('./Observation_Datas/Extinction_Curve/ext_yenhsing_stellar.dat')
    Ext_DG = np.loadtxt('./Observation_Datas/Extinction_Curve/ext_yenhsing_accretion.dat')
    ROW = Find_Lambda_ROW(0.3, Ext_DG)
    plt.plot(1/Ext_DG[:,0],Ext_DG[:,3]/Ext_DG[ROW,3],color='r',linestyle='dashed',label="Ext. curve of D.G. scenario")
    plt.plot(1/Ext_SD[:,0],Ext_SD[:,3]/Ext_SD[ROW,3],color='r',linestyle='solid',label="Ext. curve of S.D. scenario")


