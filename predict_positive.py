import matplotlib.pyplot as plt
import numpy as np

base_predict = np.loadtxt('predict_base.txt')
new_predict = np.loadtxt('predict_new.txt')

baselabel = base_predict[:,0]
newlabel = new_predict[:,0]
basepredict = base_predict[:,1]
newpredict = new_predict[:,1]
num = 0
basep = []
newp = []
for i in range(len(baselabel)):
    if(baselabel[i] == -1):
        basep.append(basepredict[i])
        newp.append(newpredict[i])
        num = num + 1

x = np.arange(num)
fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax2 = fig.add_subplot(212)
ax1.scatter(x, basep, s=10, c='b', marker="s", label='baseline')
ax1.scatter(x, newp, s=10, c='r', marker="o", label='model_18')
plt.legend(loc='upper left')
plt.show()
