from collections import deque


class Solution:
    
    
    def __init__(self):
        self.stack = deque()
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        return self.bfs_topo(adj, V)

        # visited = {}
        # for src in range(0, V):
        #     if visited.get(src, None) == None:
        #         self.dfs_topo(adj, src, visited)
        # output = []
        # while len(self.stack) != 0:
        #     top_ele = self.stack.pop()
        #     output.append(top_ele)
        # return output
            
    
    def bfs_topo(self, graph, V):
        # find the incomming routes to every vertex
        output = []
        q = deque()
        i_routes = {}
        for v in V:
            i_routes[v] = 0
        for v in V:
            for nbr in graph[v]:
                i_routes[nbr] += 1

        # check which of the vertexes have 0 incomming edges
        for v in V:
            if i_routes[v] == 0
                q.append(v)

        while q:
            ele = q.popleft()

            for nbr in graph[ele]:
                i_routes[nbr] -= 1
                if i_routes[nbr] == 0:
                    q.append(nbr)
            output.append(ele)
        return output





    def dfs_topo(self, graph, src, visited):
        visited[src] = True
        
        for nbr in graph[src]:
            if visited.get(nbr, None) == None:
                self.dfs_topo(graph, nbr, visited)
        self.stack.append(src)


sol = Solution()
V = 6
     # 0,   1,   2,  3,    4,      5
adj = [[], [3], [3], [], [0, 1], [0, 2]]
print(sol.topoSort(V, adj))
