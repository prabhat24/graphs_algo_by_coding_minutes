# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

from collections import deque

class Solution:
    
    def dfs(self, caller, src, graph, visited):
        if visited.get(src, False):
            return True
        visited[src] = True

        for nbr in graph:
            if caller != nbr:
                ans = self.dfs(src, nbr, graph, visited)
                if ans:
                    return True
        return False

    def bfs(self, src, adj, visited):
        q = deque()
        q.append(src)

        while len(q) != 0:
            ele = q.popleft()
            if not visited.get(ele, False):
                visited[ele] = True
            else:
                return 1
            for nbr in adj[ele]:
                if not visited.get(nbr, False):
                    q.append(nbr)
        return 0



    #Function to detect cycle in a directed graph.
