from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        result = []

        def backtrack(index):
            if index >= len(nums):
                result.append(solutions[:])
                return
            
            backtrack(index + 1)
            solutions.append(nums[index])
            backtrack(index + 1)
            solutions.pop()

        backtrack(0)
        return result           

               
        
        
        