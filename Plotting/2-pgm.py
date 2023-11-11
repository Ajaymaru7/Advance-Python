import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3,7])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.plot(ypoints,marker='o',ms=20,mec='r',mfc='b')

font={'family':'Times New Roman','color':'blue','size':20}
plt.title("Demo of Ploting",fontdict=font)
plt.show()




