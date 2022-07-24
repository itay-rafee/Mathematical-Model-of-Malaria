from malariaModels.MacdonaldModel import macdonald_model
from malariaModels.RossModel import ross_model
import matplotlib.pyplot as plt

a, b, c, m, r, mu2, tau_m, tau_h = 0.2, 0.5, 0.5, 5, 0.01, 0.12, 10, 21
params = a, b, c, m, r, mu2
init_val = 0.01, 0.01
t = 250
RR = ross_model(init_val, params, t)

print(RR)
R_Ih = []
R_Im = []
for i in RR:
    R_Ih.append(i[0])
    R_Im.append(i[1])

plt.plot(R_Ih, 'b', label='RR Ih')
plt.plot(R_Im, '--b', label='RR Im')
plt.legend()
# naming the x axis
plt.xlabel('time')
# naming the y axis
plt.ylabel('Prevalence')

# giving a title to my graph
plt.title('Ross model')

# function to show the plot
plt.show()


