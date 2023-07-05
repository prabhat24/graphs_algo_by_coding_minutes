
class Graph:

    def __init__(self, edge_list):
        self.edge_list = edge_list
        self.max_ele = -1
        self.min_ele = (1<<32) - 1
        for edge in edge_list:
            u, v = edge
            self.max_ele = max(self.max_ele ,max(u, v))
            self.min_ele = min(self.min_ele, min(u, v))
        self.parent = [-1] * (self.max_ele+1)


    def find(self, ele):
        """
        finds the element's set id or element earliest ansestor
        """
        if self.parent[ele] == -1:
            return ele
        return self.find(self.parent[ele])

    def union(self, ele1, ele2):
        s1 = self.find(ele1)
        s2 = self.find(ele2)

        if s1 != s2:
            self.parent[s2] = s1

    def detect_forest(self):
        for edge in self.edge_list:
            u,v = edge
            self.union(u, v)
        cnt = 0
        for k in range(self.min_ele, self.max_ele + 1):
            if self.parent[k] == -1:
                cnt += 1
                if cnt >= 2:
                    return True
        return False

if __name__ == '__main__':
    edges = [
        [0, 1],
        [0, 2],
        [3, 4],
        [4, 5]
    ] 
    g = Graph(edges)
    print(g.detect_forest())