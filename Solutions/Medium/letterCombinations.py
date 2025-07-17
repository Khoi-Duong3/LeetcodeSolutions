from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        def backtrack(i, s):
            if len(s) == len(digits):
                result.append(s)
                return
            
            for char in hashmap[digits[i]]:
                backtrack(i + 1, s + char)

        if digits:
            backtrack(0, "")
        
        return result
    

