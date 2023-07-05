from collections import deque

def color_int(ch):
    return ord(ch) - ord('a')

class Solution():

    def __init__(self):
        self.graph = {}
        self.indegree = {}


    def create_graph(self, edge):
        src, dest = edge
        adj_list = self.graph.get(src, [])
        adj_list.append(dest)
        self.indegree[dest] += 1 
        self.graph["src"] = adj_list


    def largestPathValue(self, colors, edges) -> int:
        n = 0  

        for edge in edges:
            src, dest = edge
            n = max(max(src, dest), n)

        # create the indrgree list
        # populate indegree
        for i in range(n + 1):
            self.indegree[i] = 0

        for edge in edges:
            self.create_graph(edge)

        dp = self.tsort(n, colors)
        maxa = 0
        print(dp)
        print("cols->", len(dp[0]))
        print("rows->", len(dp))
        for i in range(n+1):
            for j in range(26):
                maxa = max(maxa, dp[i][j])
        return maxa


    def tsort(self, n, colors):
        # put every node with indegree 0
        dp = [[0] * (n+1) for i in range(26)]  
        q = deque()

        for i in range(n+1):
            if self.indegree[i] == 0:
                dp[i][color_int(colors[i])] = 1
                q.append(i)

        while len(q):
            ele = q.popleft()
            for nbr in self.graph.get(ele, []):
                for ch in range(0, 26):
                    dp[nbr][ch] = max(dp[nbr][ch], dp[ele][ch] + 1 if ch == color_int(colors[nbr]) else 0)
                self.indegree[nbr] -= 1
                if self.indegree[nbr] == 0:
                    q.append(nbr)
        return dp