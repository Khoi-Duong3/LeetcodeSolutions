from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range (len(nums)):
            hashset[nums[i]] = i

        for i in range (len(nums)):
            x = target - nums[i]

            if x in hashset and hashset[x] != i:
                return [i, hashset[x]]