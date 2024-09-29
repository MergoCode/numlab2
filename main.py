import math
from tabulate import f
import matplotlib.pyplot as plt
X = [] 
Y = []
def read():
    with open("inp.txt", "r") as inputfile:
        for line in inputfile:
            x_val = float(line.split()[0])
            y_val = float(line.split()[1])
            X.append(x_val)
            Y.append(y_val)
    print(len(X), len(Y))
    return len(X)

def wkx(k, x):
    p = 1
    for i in range(k+1):
        p *= (x-X[i])
    return p
def rr(k):
    S = 0
    for i in range(k + 1):
        p = 1
        for j in range(k + 1):
            if j != i:
                p *= (X[i] - X[j])
        S += Y[i] / p
    return S


def Nn(x, N):
    S = Y[0]
    for k in range(1, N+1):
        S += wkx(k-1, x) * rr(k)
    return S
    
def main():
    N = read() - 1
    x = X[0]
    
    
    h = (X[N] - X[0]) / (20 * N)
    Nn_v = []
    wkx_v = []
    R_v = []
    X_v = []
    Y_v = []
    for j in range(20 * N + 1):
        Nn_v.append(Nn(x, N))
        wkx_v.append(wkx(N, x))
        R_v.append(abs(f(x) - Nn(x, N)))
        X_v.append(x)
        Y_v.append(f(x))
        x += h
    with open("outNn.txt", "w") as outputfile1, open("outwkx.txt", "w") as outputfile2, open("outRv.txt", "w") as outputfile3, open("outYv.txt", "w") as outputfile4:
        for j in range(20 * N + 1):
            outputfile1.write(f"{X_v[j]:f}\t{Nn_v[j]:f}\n")
            outputfile2.write(f"{X_v[j]:f}\t{wkx_v[j]:f}\n")
            outputfile3.write(f"{X_v[j]:f}\t{R_v[j]:f}\n")
            outputfile4.write(f"{X_v[j]:f}\t{Y_v[j]:f}\n")
    print(f"Максимальна похибка: {max(R_v)}")
    plt.figure(1)
    plt.plot(X, Y, '.', label="Tabulated points", color="black")
    plt.plot(X_v, Y_v, label="Original function y = sin(x)", color='lightgreen')
    plt.plot(X_v, Nn_v, '--', label="Interpolated Newton Mnogochlen", color="red")
    
    plt.title(f"Newton Interpolation with N = {N}, tabulate step h = {h * 20:.3f}")
    plt.legend(loc="lower left")

    plt.figure(2)
    plt.plot(X_v, R_v, label="Pohybka")
    plt.title("Calculation error")
    plt.legend()
    plt.show()
    


main()
