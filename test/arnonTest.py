from malariaModels.AndersonAndMayModel import anderson_and_may_model
import matplotlib.pyplot as plt

from malariaModels.ArnonModel import arnon_model

t = 250
a, b, c, r, mu1, mu2, tau_m, tau_h = 0.2, 0.5, 0.5, 0.01, 0.017, 0.12, 10, 21
params = a, b, c, r, mu1, mu2, tau_m, tau_h

d, eta_m, eta_p, n_m, s, c_s, mos, hum = 0.05, 12, 4, 3, 100, 300, 5000, 100
m_params = d, eta_m, eta_p, n_m, s, c_s, mos, hum
init_val = 0, 0.0015, 0, 0
AR = arnon_model(init_val, params, m_params, t)


AR_Eh = []
AR_Ih = []
AR_Em = []
AR_Im = []
for i in AR:
    AR_Eh.append(i[0])
    AR_Ih.append(i[1])
    AR_Em.append(i[2])
    AR_Im.append(i[3])

plt.plot(AR_Eh, 'b', label='AM Eh')
plt.plot(AR_Ih, 'g', label='AM Ih')
plt.plot(AR_Em, '--b', label='AM Em')
plt.plot(AR_Im, '--g', label='AM Im')

plt.legend()
# naming the x axis
plt.xlabel('time')
# naming the y axis
plt.ylabel('Prediction')

# giving a title to my graph
plt.title('Arnon model')

# function to show the plot
plt.show()


