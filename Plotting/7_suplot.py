import matplotlib.pyplot as plt
import numpy as np

#plot 1
x = np.array([2, 4, 6 ,8])
y = np.array([1, 3, 5, 7])

plt.subplot(1, 2, 1)
plt.plot(x, y, marker = 'p')


#plot 2
x = np.array([3,5, 7, 9 ])
y = np.array([4, 5, 7, 8])

plt.subplot(1,2,2)
plt.plot(x,y)

plt.show()
