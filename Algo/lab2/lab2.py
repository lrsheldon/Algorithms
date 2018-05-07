import sys
import random
import timeit

def Method1( x, y):
    y = bin (y).lstrip('0b')
    y[::-1]
    j = 0
    for i in range(len(y)):
        if (y[i] == '1'):
            j += x << i
    return j

def Method2( x, y):
    if (x == 0 or y == 0):
        return 0;
    if (y == 1):
        return x
    z = Method2(x,y>>1)
    if (y % 2 == 0):
        return z <<1
    else:
        return (z<<1) +x

def Method3( x, y):
    n = max(x.bit_length(), y.bit_length())
    if (n == 0):
        return 0
    if (n == 1):
        if (x == 0 or y == 0):
            return 0
        else:
            return x
    xl = x >> (n>>1)
    xr = x - (xl << (n>>1))
    yl = y >> (n>>1)
    yr = y - (yl << (n>>1))
    p1 = Method3(xl,yl)
    p2 = Method3(xr,yr)
    p3 = Method3(xl + xr, yl + yr)
    return (p1<<((n>>1)<<1)) + ((p3 - p1 - p2)<<(n>>1)) + p2

def digit( d):
    x = ""
    for i in range(int(d)):
        x = x + str(random.randint(0,9))
    return int(x)



if __name__ == "__main__":
    m1 = []
    m2 = []
    m3 = []
    for i in range(10):
        x = digit(sys.argv[1])
        y = digit(sys.argv[1])
        m1.append(timeit.timeit("Method1("+ str(x)+","+ str(y) +")",number = 1,globals = globals()))
        m2.append(timeit.timeit("Method2("+ str(x)+","+ str(y) +")",number = 1,globals = globals()))
        m3.append(timeit.timeit("Method3("+ str(x)+","+ str(y) +")",number = 1,globals = globals()))
    av1 = sum(m1)/10
    av2 = sum(m2)/10
    av3 = sum(m3)/10
    print("Method1 took an average of {0} second".format(av1))
    print("Method2 took an average of {0} seconds".format(av2))
    print("Method3 took an average of {0} seconds".format(av3))
