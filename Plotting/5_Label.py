import matplotlib.pyplot as plt
import numpy as np

x = np.array([12,23,10,25,34,20,37])
y = np.array([10,12,28,43,44,27,29])

font1={'family':'serif','color':'blue','size':20}

plt.title("Children study graph",fontdict=font1,loc='LEFT')
plt.xlabel("Average Student")
plt.ylabel("Clever Student")

plt.plot(x,y)
plt.show()
