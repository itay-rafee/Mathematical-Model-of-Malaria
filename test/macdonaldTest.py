from malariaModels.MacdonaldModel import macdonald_model
import matplotlib.pyplot as plt

a, b, c, m, r, mu2, tau_m, tau_h = 0.2, 0.5, 0.5, 20, 0.01, 0.12, 10, 21
params = a, b, c, m, r, mu2, tau_m
init_val = 0.01, 0.01, 0.01
t = [0, 1, 100, 150, 200, 250]

MC = macdonald_model(init_val, params, t)

M_Ih = []
M_Im = []
for i in MC:
    M_Ih.append(i[0])
    M_Im.append(i[2])
plt.plot(M_Ih, 'g', label='MC Ih')
plt.plot(M_Im, '--g', label='MC Im')
# plt.plot(x)
plt.legend()
# naming the x axis
plt.xlabel('time')
# naming the y axis
plt.ylabel('Prediction')

# giving a title to my graph
plt.title('Ross model')

# function to show the plot
plt.show()


