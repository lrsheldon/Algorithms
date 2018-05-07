import sys

clock = 1
cc = 0
post = []

def graph( file_name ):
    f = open(file_name)
    g = {}
    visited ={}
    time = {}
    ccnum = {}
    for line in f:
        a = line.split()
        u = a[0]
        v = a[1]
        if ( u in g ):
            g[u].append(v)
            if (v not in g):
                g[v] = []
                visited[v] = False
                time[v] = []
                ccnum[v] = []
        else:
            g[u] = [v]
            visited[u] = False
            time[u] = []
            ccnum[u] = []
            if (v not in g):
                g[v] = []
                visited[v] = False
                time[v] = []
                ccnum[v] = []
    return g,visited,time,ccnum

def reverse_graph( graph ):
    g = {}
    for k in graph.keys():
        for v in graph[k]:
            if ( v in g ):
                g[v].append(k)
                if (k not in g):
                    g[k] = []
            else:
                g[v] = [k]
                if (k not in g):
                    g[k] = []
    return g

def previsit(v,time,ccnum):
    global clock
    global cc
    ccnum[v].append(cc)
    time[v].append(clock)
    clock += 1

def postvisit(v,time):
    global clock
    global post
    time[v].append(clock)
    post.append(v)
    clock += 1

def explore(g,v,visited,time,ccnum):
    visited[v] = True
    previsit(v,time,ccnum)
    for u in g[v]:
        if (visited[u] == False):
            explore(g,u,visited,time,ccnum)
    postvisit(v,time)

def DFS( g, visited, time, ccnum):
    global cc
    cc = 0
    for v in g.keys():
        visited[v] = False
    for v in g.keys():
        if (visited[v] == False):
            explore(g,v,visited,time,ccnum)
            cc += 1

def explore_print(g,u,cc):
    visited[u] = True
    for v in g[u]:
        if (visited[v] == False):
            explore_print(g,v,cc)
            if ( v not in cc):
                cc.append(v)
    return cc



def DFS_connected(g,visited):
    global post
    for v in g.keys():
        visited[v] = False
    for u in post:
        if (visited[u] == False):
            a = explore_print(gr,u,[u])
            print(a)


if __name__ == "__main__":

    g,visited,time,ccnum = graph(sys.argv[1])

    gr = reverse_graph(g)
    
    DFS(gr,visited,time,ccnum)

    DFS_connected(g,visited)
