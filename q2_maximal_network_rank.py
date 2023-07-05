# leetcode 1615

class Solution:

    def __init__(self):
        self.graph = {}

    def create_graph(self, edge):
        src, nbr = edge
        # if src > nbr:
        #     src, nbr = nbr, src
        a = self.graph.get(src, [])
        a.append(nbr)
        b = self.graph.get(nbr, [])
        b.append(src)
        self.graph[src] = a
        self.graph[nbr] = b

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxa = 0
        for edge in roads:
            self.create_graph(edge)
        
        vertexes = list(self.graph.keys())
        N = len(vertexes)
        for i in range(0, N-1):
            for j in range(i+1 , N):
                city1_nbrs, city2_nbrs = self.graph[vertexes[i]], self.graph[vertexes[j]]
                if vertexes[i] in city2_nbrs:
                    maxa = max(len(city1_nbrs) + len(city2_nbrs) - 1, maxa)
                else:
                    maxa = max(len(city1_nbrs) + len(city2_nbrs), maxa)
        return maxa