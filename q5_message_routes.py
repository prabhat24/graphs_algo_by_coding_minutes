
from collections import deque
from sys import stdin, stdout


class Graph:

	def __init__(self):
		self.graph = {}


	def add_edge(self, edge):
		src, nbr = edge
		adj_list_src = self.graph.get(src, [])
		adj_list_nbr = self.graph.get(nbr, [])
		adj_list_src.append(nbr)
		adj_list_nbr.append(src)
		self.graph[src] = adj_list_src
		self.graph[nbr] = adj_list_nbr


	def bfs(self, visited, src, dest):

		q = deque()
		psf = str(src)
		q.append([src, 1, psf])
		
		while len(q) != 0:
			ele, level, psf = q.popleft()
			if ele == dest:
				return level, psf
			
			if not visited.get(ele, False):
				visited[ele] = True
			else:
				continue
			for nbr in self.graph.get(ele, []):
				if not visited.get(nbr, False):
					q.append([nbr, level+1, psf + " " + str(nbr)])

		return -1, ""




if __name__ == '__main__':
	n, m = [int(x.strip()) for x in stdin.readline().split()]

	edges = []
	for k in range(0, m):
		edge = [int(x.strip()) for x in stdin.readline().split()]
		edges.append(edge)
	graph = Graph()
	for edge in edges:	
		graph.add_edge(edge)
	visited = {}
	nodes, psf = graph.bfs(visited, 1, n)
	if nodes == -1:
		print("IMPOSSIBLE")
	else:
		print(nodes)
		print(psf)

