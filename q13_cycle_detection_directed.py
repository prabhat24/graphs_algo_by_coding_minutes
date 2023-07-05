class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        visited = {}
        visited_stk = {}
        for i in range(V):
            if not visited.get(i, False):
                if self.dfs(i, adj, visited, visited_stk):
                    return 1
        return 0
    
    def dfs(self, src, graph, visited, visited_stk):
        try:
            visited[src] = True
            visited_stk[src] = True
            ans1, ans2 = False, False
            for nbr in graph[src]:
                if visited_stk.get(nbr, False):
                    ans1 = True
                if ans1:
                    break
                if not visited.get(nbr, False):
                    ans2 = self.dfs(nbr, graph, visited, visited_stk)
                if ans2:
                    break
            visited_stk[src] = False
            return ans1 or ans2

        except Exception as e:
            print(e)


sol = Solution()
print(sol.isCyclic(4, [[1], [2], [3], [3]]))
