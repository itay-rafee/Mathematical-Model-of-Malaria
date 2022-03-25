from malariaModels.AndersonAndMayModel import anderson_and_may_model
from malariaModels.ArnonModel import arnon_model
from malariaModels.MacdonaldModel import macdonald_model
from malariaModels.RossModel import ross_model
import matplotlib.pyplot as plt

t = 250
a, b, c, m, r, mu1, mu2, tau_m, tau_h = 0.2, 0.5, 0.5, 20, 0.01, 0.017, 0.05, 10, 21
d, eta_m, eta_p, n_m, s, c_s, mos, hum = 0.05, 12, 4, 3, 100, 300, 5000, 100

# ====== Ross Model ======
params = a, b, c, m, r, mu2
init_val = 0.0015, 0
RR = ross_model(init_val, params, t)

R_Ih = []
R_Im = []
for i in RR:
    R_Ih.append(i[0])
    R_Im.append(i[1])

# ====== Macdonald Model ======
params = a, b, c, m, r, mu2, tau_m
init_val = 0.0015, 0, 0
MC = macdonald_model(init_val, params, t)

M_Ih = []
M_Im = []
for i in MC:
    M_Ih.append(i[0])
    M_Im.append(i[2])

# ====== Anderson and May Model ======
params = a, b, c, m, r, mu1, mu2, tau_m, tau_h
init_val = 0, 0.0015, 0, 0
AM = anderson_and_may_model(init_val, params, t)

A_Ih = []
A_Im = []
for i in AM:
    A_Ih.append(i[1])
    A_Im.append(i[3])

# ====== Arnon Model ======
params = a, b, c, r, mu1, mu2, tau_m, tau_h
m_params = mu2, eta_m, eta_p, n_m, s, c_s, mos, hum
init_val = 0, 0.0015, 0, 0
AR = arnon_model(init_val, params, m_params, t)

AR_Ih = []
AR_Im = []
for i in AR:
    AR_Ih.append(i[1])
    AR_Im.append(i[3])

# ====== Print on chart ======
plt.plot(R_Ih, 'b', label='RR Ih')
plt.plot(R_Im, '--b', label='RR Im')

plt.plot(M_Ih, 'g', label='MC Ih')
plt.plot(M_Im, '--g', label='MC Im')

plt.plot(A_Ih, 'r', label='AM Ih')
plt.plot(A_Im, '--r', label='AM Im')

plt.plot(AR_Ih, 'y', label='AR Ih')
plt.plot(AR_Im, '--y', label='AR Im')

plt.legend()
# naming the x axis
plt.xlabel('time')
# naming the y axis
plt.ylabel('Prediction')

# giving a title to my graph
# plt.title('Mathematical models of malaria')

# function to show the plot
plt.show()
