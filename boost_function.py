import matplotlib.pyplot as plt
import numpy as np

def boost_function(x, k, c1, c2, c3, c4):
    exp = np.exp(c2 * (x / 100.0 - k - c4))
    y = 1.0*(c3 + c1 * exp) / (1 + exp)
    print("y:",y)
    if c3 > c1:
        t = c3
    else:
        t = c1
    upper_bound = 2 * t
    if(0 < y and y <= upper_bound):
        return y
    else:
        return -1
        print("Invalid result: x=%s, y=%s", x, y)

if __name__ == "__main__":
    x = np.arange(73000) * 0.1
    y = np.zeros(73000)
    for i in range(73000):
        y[i] = boost_function(x[i], -200.0, 3.8, 50.0, 2.15, 260.0)
    fig = plt.figure()
    plt.legend(loc='upper left')
    plt.plot(x, y)
    plt.show()
