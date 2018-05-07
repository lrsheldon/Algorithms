import random
import math

def modexp( x, y, N):
    print( "x = {}  y = {}".format(x,y))
    if (y == 0):
        return 1
    z = modexp( x, math.floor(y/2), N)
    if (y & 1):
        return (x*(z**2)) % N
    else:
        return (z**2) % N

def prime( N, k):
    n = 0
    for i in range(k):
        a = random.randint(1,N-1)
        if (modexp(a,N-1,N) == 1):
            n += 1
    if (n == k):
        print("{} is Prime\n".format(N))
        print("{}%".format(100))
        return True
    else:
        print("{} is not prime\n".format(N))
        print("{}% of the tests returned true, but {} is in fact not prime.".format((n/k)*100,N))
        return False


if __name__ == "__main__":
    print("Compute x^y mod N")
    x = int(input("x: "))
    y = int(input("y: "))
    N = int(input("N: "))
    print("{}^{} mod {} = {}".format(x,y,N,modexp(x,y,N)))
    print("Primality Testing")
    p = int(input("Enter a number to see if it is prime: "))
    k = int(input("How many trials: "))
    prime(p,k)
    '''
    carmike = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881]
    for i in carmike:
        n = 0
        for j in range(0, 1000):
            boo= prime(i,1000)
            if (boo == True):
                n += 1
        print("{}".format(float(n)/1000))
        '''
