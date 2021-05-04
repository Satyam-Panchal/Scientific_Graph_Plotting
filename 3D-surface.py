import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm
from ipywidgets import interactive

def z_function(x, y):
    return np.sin(x) * np.cos(y)

ax = plt.axes(projection="3d")

x =np.linspace(-2, 2, 50)
y =np.linspace(-2, 2, 50)

X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)

ax.plot_surface(X, Y, Z, cmap=cm.coolwarm )
plt.show()