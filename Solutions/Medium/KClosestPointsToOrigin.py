from typing import List
from collections import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        result = []

        for x, y in points:
            distance = -(((x**2) + (y**2)) ** (1/2))
            heapq.heappush(maxHeap, [distance, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        while maxHeap:
            distance, x, y = heapq.heappop(maxHeap)
            result.append([x,y])
        
        return result




"""
What we know:
    - 2D array (matrix)
    - Coordinate system, instead of tuples it's 2 item arrays
"""