from floyd_warshall import FloydWarshall
import unittest
import numpy as np

INF  = 99999

class TopCharsTest(unittest.TestCase):

    
    def test_floydWarshall(self):
    #test graph
    #     10 
    # (0)------->(3) 
    # |         /|\ 
    # 5 |          | 
    # |          | 1 
    # \|/         | 
    # (1)------->(2) 
    #     3           

        graph = [[0,5,INF,10],[INF,0,3,INF],[INF, INF, 0,   1],[INF, INF, INF, 0]] 
        result = FloydWarshall.floydWarshall(graph)
        expected =[[ 0,5,8 ,9],[INF,0,3,4],[INF,INF,0,1],[INF,INF,INF,0]]
        self.assertEquals(result,expected)


if __name__ == "__main__":
    unittest.main()