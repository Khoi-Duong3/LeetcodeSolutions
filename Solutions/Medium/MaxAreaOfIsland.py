from collections import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col): 
            if (row < 0) or row == rows or (col < 0) or col == cols or ((row, col) in visited) or grid[row][col] == 0:
                return 0
            
            visited.add((row, col))
            return (1 + dfs(row+1, col) + dfs(row, col+1) + dfs(row-1, col) + dfs(row, col-1))


        for row in range (rows):
            for col in range (cols):
                maxArea = max(maxArea, dfs(row,col))
        
        return maxArea
        