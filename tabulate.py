import math
def f(x):
    return math.sin(x) * x 

def tabulate():
    a = 0
    
    n = 10
    h = 1
    b = a + h * n
    with open("inp.txt", "w") as inputfile:
        for i in range(n+1):
            x = a + i * h
            y = f(x)
            inputfile.write(f"{x:.5f} {y:.5f}\n")
        print("DONE")

tabulate()