from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        solutions = []

        def backtrack():
            if len(solutions) == len(nums):
                result.append(solutions[:])
                return
            
            for num in nums:
                if num not in solutions:
                    solutions.append(num)
                    backtrack()
                    solutions.pop()
        
        backtrack()
        return result
                