# https://leetcode.com/problems/redundant-connection/

class Solution:

    def find(self, ele, parent):
        """
        finds the element's set id or element earliest ansestor
        """
        if parent[ele] == -1:
            return ele
        return self.find(parent[ele], parent)

    def union(self, ele1, ele2, parent):
        s1 = self.find(ele1, parent)
        s2 = self.find(ele2, parent)

        if s1 != s2:
            parent[s2] = s1

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        max_ele = max([max(u, v) for u,v in edges])
        parent = [-1] * (max_ele + 1)
        for edge in edges:
            u,v = edge
            s1 = self.find(u, parent)
            s2 = self.find(v, parent)
            if s1 == s2:
                ans = [u,v]
            else:
                self.union(u,v, parent)
        return ans