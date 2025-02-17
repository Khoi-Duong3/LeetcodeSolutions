from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * (len(nums))
        prefix = 1
        postfix = 1
        
        for i in range (len(nums)):
            result[i] = prefix
            prefix *= nums[i]
       
        for j in range (len(nums)-1, -1, -1):
            result[j] = postfix * result[j]
            postfix *= nums[j]

        return result
