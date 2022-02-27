from malariaModels.AndersonAndMayModel import anderson_and_may_model
import matplotlib.pyplot as plt

t = [0, 1, 100, 150, 200, 250]
a, b, c, m, r, mu1, mu2, tau_m, tau_h = 0.2, 0.5, 0.5, 20, 0.01, 0.017, 0.12, 10, 21
params = a, b, c, m, r, mu1, mu2, tau_m, tau_h
init_val = 0, 0.0015, 0, 0
AM = anderson_and_may_model(init_val, params, t)


AM_Ih = []
AM_Im = []
for i in AM:
    AM_Ih.append(i[1])
    AM_Im.append(i[3])

plt.plot(AM_Ih, 'r', label='AM Ih')
plt.plot(AM_Im, '--r', label='AM Im')

plt.legend()
# naming the x axis
plt.xlabel('time')
# naming the y axis
plt.ylabel('Prediction')

# giving a title to my graph
plt.title('Ross model')

# function to show the plot
plt.show()


