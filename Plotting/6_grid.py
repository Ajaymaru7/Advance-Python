import numpy as np
import matplotlib.pyplot as plt

x = np.array([3, 5, 7 ,8 ,10, 16, 19])
y = np.array([4, 6, 8 ,14, 15, 23, 25])


font={'font':'Times New Roman','size':19}

plt.title("Graph",fontdict=font)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.plot(x,y)


plt.grid(axis = 'y',color = 'green', linestyle = '-.',linewidth =1)

plt.show()
