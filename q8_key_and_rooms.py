
class Solution:

	def __init__(self):
		self.count = 0

	def canVisitAllRooms(self, rooms):
		self.count = 0
		N = len(rooms)
		visited = {}
		self.dfs(0, visited)
		if self.count == N:
			return True
		return False


	def dfs(self, src, visited, rooms):
		visited[src] = True
		self.count += 1
		all_keys = rooms[src]
		for nbr in all_keys:
			if not visited.get(src, False):
				self.dfs(nbr, visited, rooms)



if __name__ == '__main__':
