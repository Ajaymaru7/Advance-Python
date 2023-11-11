import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([4,2,7,9,8])
ypoint = np.array([2,4,6,8,10])


plt.plot(xpoint,linewidth = '2')
plt.plot(ypoint,linestyle = 'dashdot',marker='H',color = 'b',linewidth = '3',ms=15,mec='red')
plt.show()
