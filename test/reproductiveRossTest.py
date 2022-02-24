import numpy as np  # For mathematics, and making arrays
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator
# Arrays x, y and z for data plot visualization


from malariaModels.RossModel import reproductive_number

mu2 = np.arange(0.5, 0.096, -0.004)
a = np.arange(0.01, 0.0302, 0.0002)
# meshgrid makes a retangular grid out of two 1-D arrays. 
mu2, a = np.meshgrid(mu2, a)
b, c, m, r = 0.5, 0.5, 20, 0.01
R0 = []
for i in range(len(a)):
    params = a[i], b, c, m, r, mu2[i]
    R0.append(reproductive_number(params))

z = np.array(R0)
print(len(mu2[0]))
print(len(a[0]))
print(mu2)
print(a)
print(z)
# surface plot for x^2 + y^2 
fig = plt.figure()  # creates space for a figure to be drawn

# Uses a 3d prjection as model is supposed to be 3D
axes = fig.gca(projection='3d')

# Plots the three dimensional data consisting of x, y and z 
axes.plot_surface(mu2, a, z, label='R0=1')
axes.set_xlabel("μ2")

axes.set_ylabel("a")

axes.set_zlabel("R0")
axes.view_init(30, 45)

# axes.zaxis.set_major_locator(LinearLocator(10))
# # A StrMethodFormatter is used automatically
# axes.zaxis.set_major_formatter('{x:.02f}')
# # show command is used to visualize data plot
plt.show()
