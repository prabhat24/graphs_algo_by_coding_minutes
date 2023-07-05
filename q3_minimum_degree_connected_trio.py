# leetcode 1761

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(lambda: set())
        res = float("inf")
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for k in range(j+1, n+1):
                    if j in g[i] and k in g[i] and k in g[j]: # this line judge if (i, j, k) is a trio
                        d = len(g[i]) + len(g[j]) + len(g[k]) - 6
                        res = min(res, d)
        return res if res!=float("inf") else -1