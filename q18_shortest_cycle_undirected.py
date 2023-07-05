from collections import deque

class Solution:
    
    def __init__(self):
        self.graph = {}
        self.shortest_cycle = 1<<31 - 1

    def create_graph(self, edge):
        src, dest = edge
        adj_list = self.graph.get(src, [])
        adj_list.append(dest)
        self.graph[src] = adj_list

        # as bi dir
        adj_list = self.graph.get(dest, [])
        adj_list.append(src)
        self.graph[dest] = adj_list


    #Function to detect cycle in a directed graph.
    def shortest_cycle_undirected(self, V, adj):

        visited = {}
        for edge in adj:
            self.create_graph(edge)

        for i in range(V):
            visited = {}
            self.bfs(i, visited)
        return self.shortest_cycle
    
    def bfs(self, src, visited):
        q = deque()
        q.append([src, 0])

        while len(q):
            ele, level = q.popleft()
            if visited.get(ele, None) is None:
                visited[ele] = level
            else:
                self.shortest_cycle = min(self.shortest_cycle, level + visited[ele])
            for nbr in self.graph.get(ele, []):
                if visited.get(nbr, None) is None:
                    q.append([nbr, level+1])
        return 0

sol = Solution()
adj = [
    [0, 3],
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 4]
    ]
ans = sol.shortest_cycle_undirected(7, adj)
print(ans)