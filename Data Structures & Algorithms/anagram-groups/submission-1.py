class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ''' for each word, we need to have a signature which is list of 26 0's
        if a is present twice arr[ASCII of 'a' - ASCII(char of word)] == arr[0]
        then we have a defaultdict which have same sign so we just return values of dict
        '''

        d = defaultdict(list)

        for w in strs:

            ct = [0] * 26

            for c in w:
                ct[ord(c)-ord('a')] += 1
            
            d[tuple(ct)].append(w)
        return list(d.values())


        