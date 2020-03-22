import numpy as np
import matplotlib.pyplot as plt

print("input the file you want to view: ")
Datas = np.loadtxt(input())
for i in range(0,np.shape(Datas)[0]):
    if Datas[i,6] <= 3*10**7:
        plt.scatter(Datas[i,0],Datas[i,1],c='b',s=0.1)
    else:
        plt.scatter(Datas[i,0],Datas[i,1],c='y',s=0.1)
    print(i)
#plt.xlim([-10,10])
#plt.ylim([-10,10])
plt.show()
