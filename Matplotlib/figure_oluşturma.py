import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x**3
z = x**2

"""
figure = plt.figure()
axes_cube = figure.add_axes([0.2,0.2,0.8,0.8])
axes_cube.plot(x,y,'b')
axes_cube.set_xlabel("X axis")
axes_cube.set_ylabel("Y axis")
axes_cube.set_title("cub")

axes_square = figure.add_axes([0.25,0.6,0.25,0.25])
axes_square.plot(x,z,'r')
axes_square.set_xlabel("X axis")
axes_square.set_ylabel("Y axis")
axes_square.set_title("square")
"""
"""
figure = plt.figure()
axes = figure.add_axes([0,0,1,1])
axes.plot(x,z,label = "Square")
axes.plot(x,y,label = "Cube")
axes.legend(loc=1)
"""

fig,axes = plt.subplots(nrows = 2, ncols = 1)
axes[0].plot(x,y)
axes[0].set_title("cube")
axes[1].plot(x,z)
axes[1].set_title("square")
fig.savefig("figure1.png")
fig.savefig("figure1.pdf")
plt.tight_layout()
plt.show()