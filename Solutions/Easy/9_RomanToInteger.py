class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {  'I' : 1,
                        'V' : 5,
                        'X' : 10,
                        'L' : 50,
                        'C' : 100,
                        'D' : 500,
                        'M' : 1000 }
        
        total = 0
        i = 0
        n = len(s)
        while i < n:
            if i < n-1 and dictionary[s[i]] < dictionary[s[i+1]]:
                total += dictionary[s[i+1]] - dictionary[s[i]]
                i += 2
            else:
                total += dictionary[s[i]]
                i += 1

        return total