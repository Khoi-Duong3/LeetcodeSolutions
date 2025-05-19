class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for i in range (len(magazine)):
            if magazine[i] not in letters:
                letters[magazine[i]] = 1
            else:
                letters[magazine[i]] += 1
        
        for j in range (len(ransomNote)):
            if ransomNote[j] not in letters:
                return False
            elif (letters[ransomNote[j]] == 0):
                return False
            else:
                letters[ransomNote[j]] -= 1
        return True