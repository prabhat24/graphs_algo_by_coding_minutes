
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

	def check_same_set(self, ele1, ele2):
		s1 = self.find(ele1)
		s2 = self.find(ele2)

		if s1 == s2:
			return True
		return False


if __name__ == '__main__':
	query = [[1,1,2],[1,1,3],[2,1,4],[2,2,3]] 
	max_ele = -1
	min_ele = (1<<31) -1
	
	for q in query:
		_, u, v = q
		max_ele = max(max_ele, max(u, v))
		min_ele = min(min_ele, min(u, v))
	output = []
	dsu = DSU(max_ele)
	for q in query:
		operation, u, v= q
		if operation == 1:
			dsu.union(u, v)
		elif operation == 2:
			output.append(dsu.check_same_set(u, v))
	print(output)
