from sortedcontainers import SortedList

class Solution:

    def __init__(self):
        self.graph = {}
        self.sol_order = []

    def create_graph(self, edge):
        src, dest = edge
        adj_list = self.graph.get(src, [])
        adj_list.append(dest)
        self.graph[src] = adj_list

    def findOrder(self, numCourses, prerequisites):
        for edge in prerequisites:
            self.create_graph(edge)
        visited = {}
        for icourse in range(0, numCourses):
            if not visited.get(icourse, False):
                stv = {}
                ans = self.dfs(icourse, stv, visited)
                if ans == False:
                    return []
        return self.sol_order



    def dfs(self, src, stv, visited):
        visited[src] = True
        stv[src] = True
        for nbr in self.graph.get(src, []):
            if not visited.get(nbr, False):
                ans = self.dfs(nbr, stv, visited)
                if ans == False:
                    return False
            else:
                if stv.get(nbr, False):
                    return False
        self.sol_order.append(src)
        stv[src] = False
        return True
