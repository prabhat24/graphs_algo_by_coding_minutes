from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        ans = True
        for node in range(len(graph)):
            if not visited.get(node, False):
                ans = self.bfs(node, visited, graph)
                if not ans:
                    return False
        return True

    def bfs(self, src, visited, graph):
        q = deque()
        q.append([src, 0])

        while len(q) != 0:
            ele, level = q.popleft()
            if visited.get(ele, None) is None:
                visited[ele] = level
            else:
                if visited[ele]%2 != level %2:
                    return False
            for nbr in graph[ele]:
                if visited.get(nbr, None) is None:
                    q.append([nbr, level+1])
        return True


    # using colouring 
    def dfs(self, src, parent, visited, color, graph):
        visited[src] = color

        for nbr in graph[src]:
            if nbr == parent:
                continue
            # for not parent and visited 
            elif nbr != parent and visited.get(nbr, None) is not None:
                if visited[nbr] == color:
                    return False
            elif visited.get(nbr, None) is None:
                if self.dfs(nbr, src, visited, 3-color, graph) == False:
                    return False
        return True