#!/usr/bin/env python3



#A function that will create the graph will take in: k (int) and sets (list) and will return the graph
def createGraph(k, sets):
    newGraph = {}
    for i in sets:
        for v in i:
            newGraph[v] = []
    return newGraph

#This function will create the edges of the grpah
def add_edge(graph,edges):
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

#This function helps simply the graph, takes in graph as an argument, outputs a simplified graph
#It implemnets the unit rule of eliminating verticies with only one possible match (unit rule)
def fixGraph(newGraph):
    change = True
    while change:
        change = False
        removeFrom = []
        for v in list(newGraph.keys()):
            if len(newGraph[v]) == 0:
                removeFrom.append(v)
                change = True
            elif len(newGraph[v]) == 1:
                u = newGraph[v][0]
                removeFrom.append(v)
                removeFrom.append(u)
                change = True
        for v in removeFrom:
            if v in newGraph:
                for n in newGraph[v]:
                    if n in newGraph:
                        newGraph[n].remove(v)
                del newGraph[v]
    return newGraph

#Function that uses Depth First Search (DFS) to find perfect macthes 
def matchableGraph(v, newGraph, match, visit):
    for n in newGraph[v]:
        if visit[n]:
            continue
        visit[n] = True
        if n not in match or matchableGraph(match[n], newGraph, match, visit):
            match[n] = v
            return True
    return False

#This function is the matching algorithm, takes in the graph and returns bool, calls the function that performs rules
def matchingFunc(newGraph):
    newGraph = fixGraph(newGraph)
    for v in newGraph.keys():
        if len(newGraph[v]) == 0:
            return False

    match = {}
    for v in newGraph.keys():
        visit = {a: False for a in newGraph.keys()}
        if not matchableGraph(v,newGraph,match,visit):
            return False

        if len(match) == len(newGraph) //2:
            return True
        else:
            return False
    
    return True


    
    

    





#test
if __name__ == "__main__":
    sets =  [[1, 2], [3, 4]]
    newGraph = createGraph(4, sets)
    edges = [(1, 3), (1, 4), (2, 3), (2, 4)]
    add_edge(newGraph,edges)
    print("Initial Graph:", newGraph)
    result = matchingFunc(newGraph)
    print("After Graph:", newGraph)
    if result:
        print("Perfect match exists")
    else:
        print("perfect match does not exist")
