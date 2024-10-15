#!/usr/bin/env python3



#A function that will create the graph will take in: k (int) and sets (list) and will return the graph
def createGraph(k, sets):
    newGraph = {}
    for i in sets:
        for v in i:
            newGraph[v] = []
    return newGraph

#This function will create the edges
def add_edge(graph,edges):
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

#This function helps simply the graph, takes in graph as an argument, outputs a simplified graph
def fixGraph(newGraph):
    change = True
    while change:
        change = False
        removeFrom = []
        for v in list(newGraph.keys()):
            if len(newGraph[v]) == 1:
                u = newGraph[v][0]
                removeFrom.append(v)
                removeFrom.append(u)
                chnages = True
        for v in removeFrom:
            if v in newGraph:
                for n in newGraph[v]:
                    newGraph[n].remove(v)
                del newGraph[v]
    return newGraph

#This function is the matching algorithm, takes in the graph and returns bool
def matchingFunc(newGraph):
    newGraph = fixGraph(newGraph)
    if len(newGraph) == 0:
        return True #perfect
    else:
        return False #not perfect


#test
if __name__ == "__main__":
    sets = [[1,2],[3,4],[5,6]]
    newGraph = createGraph(3, sets)
    edges = [(1,3),(2,4),(3,5),(4,6)]
    add_edge(newGraph,edges)
    result = matchingFunc(newGraph)
    if result:
        print("Perfect match exists")
    else:
        print("perfect match does not exist")
