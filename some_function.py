import matplotlib.pyplot as plt
import numpy as np

UBOUND_ARGX_EXP = 700
def _safe_exp(x):
    if x < 700:
        return np.exp(x)
    else:
        return np.exp(700)

def function_1(x, k, c1, c2, c3, c4):
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

def function_2(x, rf, u, tp, k, coef_01, coef_02, coef_03):
    exp_a = _safe_exp(coef_01 * (tp - coef_02))
    exp_b = _safe_exp(- coef_03 * (x / 100 - k))
    f = (
        1 + (0.95 * rf / u + exp_a) / (1 + exp_a) * exp_b
    ) / (
        1 + exp_b
    );
    #y = rf - u * f;
    return f


if __name__ == "__main__":
    # function 1
    #x = np.arange(0, 300) * 1.0
    #y = np.zeros(300)
    #y1 = np.zeros(300)
    #y2 = np.zeros(900)
    #y3 = np.zeros(900)
    #y4 = np.zeros(900)
    #for i in range(300):
    #    pass
    #    y[i] = function_1(x[i], -121.79645156272358, 2.4, 10.0, 3.7, 122.3)
    #    y1[i] = function_1(x[i], -121.79645156272358, 2.4, 10.0, 3.7, 122.4)
        #y2[i] = function_1(x[i], -121.79645156272358, 3.0, 10.0, 3.2, 124)
        #y3[i] = function_1(x[i], -121.79645156272358, 3.0, 10.0, 3.2, 125)
        #y4[i] = function_1(x[i], -121.79645156272358, 3.0, 10.0, 3.2, 126)
        #pc yes y[i] = function_1(x[i], -121.79645156272358, 3.3, 50.0, 2.8, 180.0)
        #sp not y[i] = function_1(x[i], -200, 5.2, 15.0, 4.6, 8.5)
        #sp yes y[i] = function_1(x[i], -200, 3.8, 50.0, 2.15, 260)

    #function 2
    x = np.arange(0, 1000) * 1.0
    y = np.zeros(1000)
    for i in range(1000):
        y[i] = function_2(x[i], 0.6, 0.4012996020240296, -2.657946349575869E-9, -121.79645156272358, 5.0, 1.0, 5.0)

    fig = plt.figure()
    plt.plot(x, y)
    #plt.plot(x, y1)
    #plt.plot(x, y2)
    #plt.plot(x, y3)
    #plt.plot(x, y4)
    plt.legend(loc='upper left')
    plt.show()
