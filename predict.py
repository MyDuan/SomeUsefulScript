import matplotlib.pyplot as plt
import numpy as np

base_predict = np.loadtxt('predict_base.txt')[:,1]
new_predict = np.loadtxt('predict_new.txt')[:,1]

count = len(base_predict)
x = np.arange(count)
fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax2 = fig.add_subplot(212)
ax1.scatter(x, base_predict, s=10, c='b', marker="s", label='baseline')
ax1.scatter(x, new_predict, s=10, c='r', marker="o", label='model_18')
plt.legend(loc='upper left');
plt.show()
