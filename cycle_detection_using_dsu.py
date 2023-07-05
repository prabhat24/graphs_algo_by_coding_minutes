
class DSU:

	def __init__(self, N):
		self.parent = [-1] * (N+1)


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


	def is_cycle_present(self, edge_list):
		for edge in edge_list:
			ele1, ele2 = edge
			s1 = self.find(ele1)
			s2 = self.find(ele2)
			if s1 != s2:
				self.union(s1, s2)
			else:
				return True
		return False



if __name__ == '__main__':
	n = 4
	dsu = DSU(n)
	edge_list = [[1, 2], [2,3], [3,4], [4,1]]
	print(dsu.is_cycle_present(edge_list))