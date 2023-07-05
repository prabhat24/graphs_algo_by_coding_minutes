
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

	def merge(self, ele1, ele2):
		s1 = self.find(ele1)
		s2 = self.find(ele2)

		if s1 != s2:
			self.parent[s2] = s1


if __name__ == '__main__':
	n = 4
	dsu = DSU(4)
	dsu.merge(1,4)
	dsu.merge(2,3)
	print(dsu.find(1))
	print(dsu.find(2))
	print(dsu.find(3))
	print(dsu.find(4))