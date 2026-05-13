from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ct, cs = Counter(t), Counter(s)
        return ct == cs
        
        
        

        

        