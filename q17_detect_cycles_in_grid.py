# leetcode -> https://leetcode.com/problems/detect-cycles-in-2d-grid/discussion/

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        C = len(grid[0])
        R = len(grid)
        visited = [[0] * C for i in range(R)]
        for i in range(0, R):
            for j in range(0, C):
                if visited[i][j] == 0:
                    if self.dfs(i, j, grid, visited, R, C, -1, -1):
                        return True
        return False


    def dfs(self, srcr, srcc, grid, visited, R, C, par_r, par_c):
        visited[srcr][srcc] = 1

        paths = [ [0, 1], [1, 0], [0, -1], [-1, 0] ]
        for pr, pc in paths:
            if srcr + pr >= 0 and srcr + pr < R and srcc + pc >= 0 and srcc + pc < C \
                    and grid[srcr + pr][srcc + pc] == grid[srcr][srcc]:
                if visited[srcr + pr][srcc + pc] and [srcr + pr, srcc + pc] != [par_r, par_c]:
                    return True
                elif visited[srcr + pr][srcc + pc] == 0: 
                    if self.dfs(srcr + pr, srcc + pc, grid, visited, R, C, srcr, srcc):
                        return True
        return False
                
                
