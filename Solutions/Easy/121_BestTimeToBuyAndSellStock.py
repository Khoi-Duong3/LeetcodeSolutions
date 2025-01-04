from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in prices[1:]:
            if i > buy:
                profit = max(profit, i - buy)
            else: 
                buy = i
        
        return profit