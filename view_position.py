import numpy as np
import matplotlib.pyplot as plt

print("input the file you want to view: ")
Datas = np.loadtxt(input())
plt.scatter(Datas[:,0],Datas[:,1],s=0.1)
#plt.xlim([-10,10])
#plt.ylim([-10,10])
plt.show()
