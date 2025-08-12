class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def countWays(num):
            if num <= 2:
                return num
            
            if num not in memo:
                memo[num] = countWays(num - 1) + countWays(num - 2)
            
            return memo[num]
            
        return countWays(n)