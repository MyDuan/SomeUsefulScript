import matplotlib.pyplot as plt
import numpy as np

RLS = 0
LMS = 1

def RLS_Or_LMS(x, select):
    T = len(x)                 #number of data
    lamuda = 0.99              #forgetting factor
    s = 1.4E-45                #small positive constant
    u = 0.0001                 #u in LMS method selected arbitrary
    e = np.zeros(T)            #error
    k = np.zeros((1, 2))       #parameter k
    h = np.zeros((T, 2))       #model parameter
    P = np.eye(2)/s            #middle parameter
    X = np.zeros((1, 2))       #input

    for j in range(0, T-2):    # main Loop

        n = j + 2
        X = np.array([x[n-1], x[n-2]])
        e[j] = x[n] - (h[j][0]*X[0]+h[j][1]*X[1])
        if select == RLS:      # using the RLS method
            k = np.dot(P, X.reshape(2,1))/(lamuda + np.dot(np.dot(X.reshape(2,1).T, P), X.reshape(2,1)))
            P = (P-np.dot(k.reshape(2,1), np.dot(X.T, P).reshape(1,2)))/lamuda
        if select == LMS:      # using the MLS method
            k = 2*0.00001*X

        h[j+1] = h[j] + e[j]*k.reshape(2)
    
    
    x_test = np.zeros(T)                                #predict values using the fitted parameters
    for j in range(0, T-2):
        n = j + 2
        x_test[n] = h[j][0]*x[n-1]+h[j][1]*x[n-2]       #calculate the Predict values

    plt.figure(1)                                       #show h0, h1 and error
    Ax1 = plt.subplot(311)
    Ax2 = plt.subplot(312)
    Ax3 = plt.subplot(313)
    t = np.linspace(0, T-2, T-2)

    plt.sca(Ax1)
    plt.title("h0")
    plt.plot(t, h[0:T-2, 0], color="red")
    plt.sca(Ax2)
    plt.title("h1")
    plt.plot(t, h[0:T-2, 1], color="blue")
    plt.sca(Ax3)
    plt.title("e")
    plt.plot(t, e[0:T-2])
    
    t_part = np.linspace(0, 500, 500)

    plt.figure(2)                                      #show predict values
    plt.plot(t_part, x_test[2:502], color="red")
    plt.plot(t_part, x[2:502], color="blue")
    plt.legend()
    plt.show()
    print("Finished!")


if __name__ == "__main__":

    f = open("data.txt")
    x = []
    while 1:
        line = f.readline()
        if line:
            x.append(float(line))
        else:
            break
    #select = RLS                                      #RLS method was selected
    select = LMS                                     #LMS method was selected
    RLS_Or_LMS(x, select)

    print("The main function finished!")