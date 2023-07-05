from sortedcontainers import SortedList
from functools import reduce

class Solution:

    def __init__(self):
        self.graph = {}
        self.count = 0

    def create_graph(self, edge):
        src, dest = edge
        new_sorted_list = SortedList()
        adj_list = self.graph.get(src, new_sorted_list)
        adj_list.add(dest)
        self.graph[src] = adj_list

    def findItinerary(self, tickets):
        for ticket in tickets:
            self.create_graph(ticket)
        src = "JFK"
        ans, psfans = self.dfs(src, src, len(tickets))
        return psfans

    def dfs(self, src, psf, E):
        if self.count == E:
            return True, psf.split("-")
        sl_src = self.graph.get(src)
        if sl_src:
            for i in range(0, len(sl_src)):
                nbr = sl_src.pop(i)
                self.count += 1
                ans, psfans = self.dfs(nbr, psf + "-" + nbr, E)
                if ans == True:
                    return ans, psfans
                sl_src.add(nbr)
                self.count -= 1

        return False, ""