import matplotlib.pyplot as plt
import timeit

def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n-1) + fib1(n-2)

if __name__ == "__main__":
    inputs = [1,5,10,15,20,25,30,35]
    time = []
    for i in inputs:
        time.append( timeit.timeit("fib1("+str( i) +")","from __main__ import fib1",number = 1))
    plt.plot(inputs,time)
    plt.show()
