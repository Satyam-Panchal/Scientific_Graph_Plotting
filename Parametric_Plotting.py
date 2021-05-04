import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection="3d")

parameter = np.linspace(-10, 10, 100)

x = np.sin(parameter)
y = np.cos(parameter)
z = parameter

ax.plot3D(x, y, z)
plt.show()