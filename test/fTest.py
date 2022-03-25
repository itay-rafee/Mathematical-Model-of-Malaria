from matplotlib import pyplot as plt
from malariaModels.ArnonModel import smoothing, total_eggs

params_m = 0.05, 12, 4, 3, 100, 300, 2000, 100
t = 145
tot = total_eggs(params_m, t)
r = smoothing(tot, 0.3)

plt.plot(tot)
plt.plot(r)  # some noise removed
plt.legend()
# naming the x axis
plt.xlabel('time')
# naming the y axis
plt.ylabel('number of eggs')

# giving a title to my graph
plt.title('f parameter')

# function to show the plot
plt.show()