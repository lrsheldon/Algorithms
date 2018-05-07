import matplotlib.pyplot as plt
import timeit

def fib2(n):
    if n == 0:
        return 0
    f = [0 for i in range(n+1)] 
    f[1] = 1
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

if __name__ == "__main__":
    inputs = [2**10,2**12,2**14,2**16,2**18,2**19]
    time = []
    for i in inputs:
        time.append( timeit.timeit("fib2("+str( i) +")","from __main__ import fib2",number = 1))
    plt.plot(inputs,time)
    plt.show()
