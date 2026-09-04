class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = 0
        ans = 0
        num_s = set(nums)
        for n in nums:
            if n-1 not in num_s:
                l = 1
                while n+l in num_s:
                    l += 1
            ans = max(ans, l)
        return ans



        


        

        

        


        

        
        



        