from collections import deque
import heapq

class Edge:
    def __init__(self, src, dest, wt, t):
        self.src = src
        self.dest = dest
        self.wt = wt
        # alice 1, bob 2, both 3
        self.type = t

class Solution:


    def __init__(self):
        self.graph = {}

    def create_edge(self, edge):
        t, src, dest = edge
        e = None
        if t == 1 or t == 2:
            e = Edge(src, dest, 2, t)
        elif t == 3:
            e = Edge(src, dest, 1, t)
        adj_list = self.graph.get(src, [])
        adj_list.append(e)
        self.graph[src] = adj_list

        adj2_list = self.graph.get(dest, [])
        adj2_list.append(e)
        self.graph[dest] = adj2_list


    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        for edge in edges:
            self.create_edge(edge)
        visiteda = {}
        visitedb = {}
        count_edge = self.bfs_prism(n, visiteda, visitedb)
        return len(edges - count_edge)
    
    
    def bfs_prism(self, n, visiteda, visitedb):
        
        src = 0
        q = []
        # $, src, parent, type 
        heapq.heappush(q, [0, src, -1, -1])
        count_edges = 0
        while len(q):
            cost, ele, parent, ty = heapq.heappop()
            if visiteda.get(ele, False) and visitedb.get(ele, False):
                continue
            elif:
                if ty == 1:
                    visiteda[ele] = True
                elif ty == 2:
                    visitedb[ele] = True
                else:
                    visiteda[ele] = True
                    visitedb[ele] = True
            if parent != -1:
                count_edges += 1
            for edge in self.graph.get(ele):
                if visiteda.get(edge.src, False) and visitedb.get(edge.src, False):
                   continue
                else:
                    heapq.heappush(q, [edge.wt, edge.nbr, edge.src, edge.type])
        return count_edges
            

