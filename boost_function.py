import matplotlib.pyplot as plt
import numpy as np

UBOUND_ARGX_EXP = 700
def _safe_exp(x):
    if x < 700:
        return np.exp(x)
    else:
        return np.exp(700)

def boost_function(x, k, c1, c2, c3, c4):
    exp = _safe_exp(c2 * (x / 100.0 - k - c4))
    y = 1.0*(c3 + c1 * exp) / (1 + exp)
    if c3 > c1:
        t = c3
    else:
        t = c1
    upper_bound = 2 * t
    if(0 < y and y <= upper_bound):
        return y
    else:
        return -1

if __name__ == "__main__":
    x = np.arange(500000) * 0.0001
    y = np.zeros(500000)
    for i in range(500000):
        y[i] = boost_function(x[i], -121.79645156272358, 3.0, 10.0, 2.8, 13.7)
    fig = plt.figure()
    plt.title("spot_score-boost function")
    plt.plot(x, y)
    plt.legend(loc='upper left')
    plt.show()
