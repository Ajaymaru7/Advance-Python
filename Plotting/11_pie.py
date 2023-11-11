import matplotlib.pyplot as plt
import numpy as np

y = np.array([25,35,15,25])
L = ["C++","java","Android",".net"]
E = [0.3,0,0,0]

plt.pie(y,labels = L, startangle = 90,explode = E,shadow = True)
plt.legend(title = "Languages")
plt.show()
