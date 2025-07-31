from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        queue = deque()

        def bfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or (row,col) in visited or grid[row][col] == -1:
                return
            visited.add((row,col))
            queue.append([row,col])


        for r in range (rows):
            for c in range (cols):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r,c))
        
        distance = 0
        while queue:
            for i in range (len(queue)):
                r, c = queue.popleft()
                grid[r][c] = distance
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            
            distance += 1