class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word))+'#'+word
        
        return res

    def decode(self, s: str) -> List[str]:
        """ 
        we just need to traverse that string properly and
        append to the list and return that list
        """
        res = []
        i = 0

        while i < len(s):
            j = i
            # j will move till it reaches #
            while s[j]!= '#':
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
            

        
