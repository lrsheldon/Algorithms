
def word_matrix(l1, l2):
    L = []
    row = []
    for i in range(0,l1):
        for j in range(0,l2):
            row.append(0)
        L.append(row)
        row = []
    return L

def edit_distance(x, y):
    x = "-"+x
    y = "-"+y
    wl1 = len(x)
    wl2 = len(y)
    L = [[-1 for i in range(wl2)] for j in range(wl1)]
    back = {}
    for i in range(wl1):
        L[i][0] = i
    for j in range(wl2):
        L[0][j] = j
    for i in range(wl1):
        for j in range(wl2):
            if L[i][j] == -1:
                L[i][j] = min( L[i-1][j-1] + cost(x[i],y[j]),
                        L[i-1][j] + 1, L[i][j-1] + 1)
                if L[i][j] == L[i-1][j-1] + cost(x[i],y[j]):
                    back[(i,j)] = 1
                elif L[i][j] == L[i-1][j] + 1:
                    back[(i,j)] = 2
                elif L[i][j] == L[i][j-1] + 1:
                    back[(i,j)] = 3
            else:
                back[(i,j)] = 1
    x = x[1:]
    y = y[1:]
    return L,back,L[wl1-1][wl2-1]

def cost(x,y):
    if x == y:
        return 0
    else:
        return 1

def path(x,y,back):
    i = (len(x),len(y))
    x = x[::-1]
    y = y[::-1]
    xn = ""
    yn = ""
    j = 0
    k = 0
    while i != (0,0) and k < len(y) and j < len(x):
        if back[i] == 1:
            i = (i[0]-1,i[1]-1)
            xn += x[j]
            yn += y[k]
            j += 1
            k += 1
        elif back[i] == 2:
            i = (i[0]-1,i[1])
            xn += x[j]
            yn += "-"
            j += 1
        elif back[i] == 3:
            i = (i[0],i[1]-1)
            xn += "-"
            yn += y[k]
            k += 1
    if j != len(x):
        while j < len(x):
            xn += x[j]
            yn += "-"
            j += 1
    elif k < len(y):
        while k < len(y):
            xn += "-"
            yn += y[k]
            k += 1
    xn = xn[::-1]
    yn = yn[::-1]
    print(xn)
    print(yn)




if __name__ == "__main__":
    x = input("Enter X: ")
    y = input("Enter Y: ")

    L,back,d = edit_distance(x,y)
    
    print("Edit distance: {}".format(d))
    path(x,y,back)
