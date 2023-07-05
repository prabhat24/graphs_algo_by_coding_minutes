# Course Schedule 
# leetcode -> https://leetcode.com/problems/course-schedule/



class Solution:
    def create_graph(self, edge):
        dest, src = edge
        adj_list = self.graph.get(src, [])
        adj_list.append(dest)
        self.graph[src] = adj_list
        

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = {}
        for req in prerequisites:
            self.create_graph(req)
        visited = {}
        for s_course in range(0,numCourses):
            visited_stk = {}
            if not visited.get(s_course, False):
                if not self.dfs(s_course, visited, visited_stk):
                    return False
        return True

    def dfs(self, src, visited, visited_stk):
        visited[src] = True
        visited_stk[src] = True

        for nbr in self.graph.get(src, []):
            if visited_stk.get(nbr):
                return False
            if not visited.get(nbr, False):
                ans = self.dfs(nbr, visited, visited_stk)
                if ans == False:
                    return False
        visited_stk[src] = False
        return True
