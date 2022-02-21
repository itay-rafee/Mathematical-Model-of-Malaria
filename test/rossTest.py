from malariaModels.rossModel import ross_model
import matplotlib.pyplot as plt

a, b, c, m, r, mu2 = 0.2, 0.5, 0.5, 20, 0.01, 0.12
params = a, b, c, m, r, mu2
init_val = 0.01, 0.01
t = [0, 1, 100, 150, 200, 250]
x = ross_model(init_val, params, t)
print(x)
Ih = []
Im = []
for i in x:
    Ih.append(i[0])
    Im.append(i[1])
plt.plot(Ih, label='Ih Prediction')
plt.plot(Im, label='Im Prediction')
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


