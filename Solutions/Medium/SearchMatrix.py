from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outerLow = 0
        outerHigh = len(matrix) - 1
        outerMid = 0
        while outerLow <= outerHigh:
            outerMid = (outerLow + outerHigh) // 2
            if target > max(matrix[outerMid]):
                outerLow = outerMid + 1
            elif target < min(matrix[outerMid]):
                outerHigh = outerMid - 1
            else:
                break

        if (outerHigh < outerLow):
            return False

        innerLow = 0
        innerHigh = len(matrix[0])
        while innerLow <= innerHigh:
            innerMid = (innerHigh + innerLow) // 2
            if target > matrix[outerMid][innerMid]:
                innerLow = innerMid + 1
            elif target < matrix[outerMid][innerMid]:
                innerHigh = innerMid - 1
            else:
                return True
        
        return False
            