import numpy as np 
INF  = 99999

class FloydWarshall:

    @classmethod
    def floydWarshall(cls,graph): 
    
        dist = graph
        V = len(graph)
        for k in range(V):   
            for i in range(V): 
                for j in range(V): 
                    dist[i][j] = min(dist[i][j] , dist[i][k]+ dist[k][j])
        return dist    
    
    # A utility function to print the solution
    @classmethod 
    def printSolution(cls, dist):
        V = len(dist)
        for i in range(V): 
            for j in range(V): 
                if(dist[i][j] == INF): 
                    print("INF") 
                else: 
                    print (dist[i][j]), 
                if j == V-1: 
                    print( "" )
