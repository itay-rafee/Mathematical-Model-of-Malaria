from malariaModels.AndersonAndMayModel import anderson_and_may_model
import matplotlib.pyplot as plt

t = 250
a, b, c, m, r, mu1, mu2, tau_m, tau_h = 0.2, 0.5, 0.5, 20, 0.01, 0.017, 0.12, 10, 21
params = a, b, c, m, r, mu1, mu2, tau_m, tau_h
init_val = 0, 0.0015, 0, 0
AM = anderson_and_may_model(init_val, params, t)


AM_Eh = []
AM_Ih = []
AM_Em = []
AM_Im = []
for i in AM:
    AM_Eh.append(i[0])
    AM_Ih.append(i[1])
    AM_Em.append(i[2])
    AM_Im.append(i[3])

plt.plot(AM_Eh, 'b', label='AM Eh')
plt.plot(AM_Ih, 'g', label='AM Ih')
plt.plot(AM_Em, '--b', label='AM Em')
plt.plot(AM_Im, '--g', label='AM Im')

plt.legend()
# naming the x axis
plt.xlabel('time')
# naming the y axis
plt.ylabel('Prevalence')

# giving a title to my graph
plt.title('Anderson and May model')

# function to show the plot
plt.show()


