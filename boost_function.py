import matplotlib.pyplot as plt
import numpy as np

def boost_function(x, k, coef_04, coef_05, coef_06, coef_07):
    exp = np.exp(coef_05 * (x / 100 - k - coef_07))
    boost = (coef_06 + coef_04 * exp) / (1 + exp)
    upper_bound = 2 * (coef_06 > coef_04 ? coef_06 : coef_04)
    if(0 < $boost && $boost <= $upper_bound):
        return boost
    else
        print("Invalid result: x=%s, boost=%s", x, boost)

def main():

    boost_function()
