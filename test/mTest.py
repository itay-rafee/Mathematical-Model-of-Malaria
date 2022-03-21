
from matplotlib import pyplot as plt
from malariaModels.ArnonModel import get_m_array, smoothing

params_m = 0.05, 12, 4, 3, 100, 300, 2000, 100
t = 145
m = get_m_array(params_m, t)
r = smoothing(m)

plt.plot(m)
plt.plot(r)  # some noise removed
plt.legend()
# naming the x axis
plt.xlabel('time')
# naming the y axis
plt.ylabel('Prediction')

# giving a title to my graph
plt.title('m parameter')

# function to show the plot
plt.show()