#Importing modules
import numpy as np
import pandas as pd

P = pd.read_csv("Parameters.csv",index_col=0)
#===============================#

#Total mass of the system (Msun)
M_all = float(P.loc["M_total"]*(1-P.loc["f_clumps"]))

#Total amount of particles
n = int(P.loc["n_s"])

#Smoothing length (pc)
#R_s = float(P.loc["R_s_s"])

#The radius of the galaxy (pc)
R_g = float(P.loc["R_g"])

#Metallicity of the galaxy
#z = float(P.loc["z_s"])

#===============================#

#List of the particles
Datas = np.zeros((n,3))

#===============================#

#Making xyz postion

k = n

while k > 0:
    p = (np.random.rand(3)-np.array([0.5,0.5,0.5]))*np.array([R_g,R_g,R_g])*2
    if np.linalg.norm(p) < R_g:
        Datas[n-k,0:3] = p
        k -= 1

#===============================#

#Just for now
'''
Datas[:,3] = R_s
Datas[:,4] = M_all/n
Datas[:,5] = z
'''
#===============================#

#Saving Datas as a txt file

np.savetxt("sphere_position.txt",Datas)
