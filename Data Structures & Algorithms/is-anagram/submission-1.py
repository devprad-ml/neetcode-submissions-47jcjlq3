from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = Counter()
        map2 = Counter()
        for t, ct in zip(t, s):
            map1[t] += 1
            map2[ct] += 1
        return map1 == map2
        
        
        

        

        