import numpy as np

Rg = 7000
fc = 0.05
Nc = 100
Contrast = 50

Rc = (Rg**3*fc/Contrast/Nc/(1-fc))**(1/3)
print(Rc)

tau_s = (1-fc)/Rg**2
#print('tau_s: '+str(tau_s))

tau_c = fc/Nc/Rc**2
print('tau_s/tau_c: '+str(tau_s/tau_c))




