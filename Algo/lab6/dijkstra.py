import sys
from heapdict import heapdict

def graph( file_name ):
    f = open(file_name)
    g = {}
    for line in f:
        a = line.split()
        u = int(a[0])
        v = int(a[1])
        w = int(a[2])
        if ( u in g ):
            g[u].append([v,w])
            if (v not in g):
                g[v] = []
        else:
            g[u] = [[v,w]]
            if (v not in g):
                g[v] = []
    return g


def dijkstra ( g,s ):
    dist = {}
    prev = {}
    for u in g.keys():
        dist[u] = 1000000
        prev[u] = -1
    dist[s] = 0

    hd = heapdict()
    for u in g.keys():
        hd[u] = dist[u]
    while (len(hd) > 0):
        u = hd.popitem()
        for u in g.keys():
            for e in g[u]:
                if dist[e[0]] > dist[u] + e[1]:
                    dist[e[0]] = dist[u] + e[1]
                    prev[e[0]] = u
    return dist, prev

def path( prev, n, s ):
    u = n
    path = []
    path.append(u)
    while (u != s):
        u = prev[u]
        path.append(u)
    path.reverse()
    return path

def paths( prev, s):
    paths = {}
    for u in prev.keys():
        paths[u] = path(prev,u,s)
    return paths
        

if __name__ == "__main__":

    g = graph(sys.argv[1])

    dist,prev = dijkstra(g,1)

    paths = paths(prev,1)

    for u in dist.keys():
        print("{}: {}, {}".format(u,dist[u],paths[u]))
