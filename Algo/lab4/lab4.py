import random

def selection( A, k): #A is an array and k is the 
    z = random.randint(0,len(A)-1)
    v = A[z]
    Al = []
    Ar = []
    Av = []
    for i in range(len(A)):
        if (A[i] < v):
            Al.append(A[i])
        if ( A[i]==v):
            Av.append(A[i])
        else:
            Ar.append(A[i])
    if ( k <= len(Al)):
        return selection(Al,k)
    if ( k > len(Al) and k <= len(Al) + len(Av)):
        return v
    else:
        return selection(Ar, k-len(Al)-len(Av))
        
def randarr( n ):
    A = []
    for i in range(n):
        A.append(random.randint(0,n-1))
    return A

if __name__ == "__main__":
    n = int(input("Specify the length of the array: "))
    k = int(input("Finding the k-th element\nInput k: "))
    S = randarr( n )
    print("select {}".format(selection(S, k)))
    print("array {}".format(S))
    S.sort()
    print("sorted array {}".format(S))
