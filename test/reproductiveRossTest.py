import numpy as np  # For mathematics, and making arrays
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator
# Arrays x, y and z for data plot visualization
from malariaModels.AndersonAndMayModel import anderson_and_may_reproductive_number
from malariaModels.MacdonaldModel import macdonald_reproductive_number
from malariaModels.RossModel import reproductive_number

mu2 = np.arange(0.5, 0.096, -0.004)
a = np.arange(0.01, 0.0302, 0.0002)
# meshgrid makes a retangular grid out of two 1-D arrays. 
mu2, a = np.meshgrid(mu2, a)
b, c, m, r, mu1, tau_m, tau_h = 0.5, 0.5, 20, 0.01, 0.017/365, 10, 21
RR_R0 = []
for i in range(len(a)):
    params = a[i], b, c, m, r, mu2[i]
    RR_R0.append(reproductive_number(params))

MC_R0 = []
for i in range(len(a)):
    params = a[i], b, c, m, r, mu2[i], tau_m
    MC_R0.append(macdonald_reproductive_number(params))


AM_R0 = []
for i in range(len(a)):
    params = a[i], b, c, m, r, mu1, mu2[i], tau_m, tau_h
    AM_R0.append(anderson_and_may_reproductive_number(params))


RR_z = np.array(RR_R0)
MC_z = np.array(MC_R0)
AM_z = np.array(AM_R0)
# surface plot for x^2 + y^2 
fig = plt.figure()  # creates space for a figure to be drawn

# Uses a 3d prjection as model is supposed to be 3D
axes = fig.gca(projection='3d')

# Plots the three dimensional data consisting of x, y and z 
axes.plot_surface(mu2, a, RR_z, label='R0=1')
axes.plot_surface(mu2, a, MC_z, label='R0=1')
axes.plot_surface(mu2, a, AM_z, label='R0=1')
axes.set_xlabel("μ2")

axes.set_ylabel("a")

axes.set_zlabel("R0")
axes.view_init(5, 65)

# axes.zaxis.set_major_locator(LinearLocator(10))
# # A StrMethodFormatter is used automatically
# axes.zaxis.set_major_formatter('{x:.02f}')
# # show command is used to visualize data plot
plt.show()
