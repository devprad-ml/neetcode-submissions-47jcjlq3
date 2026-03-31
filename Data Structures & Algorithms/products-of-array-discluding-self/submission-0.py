class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)    # to store left product
        p = s = 1

        for i in range(len(nums)):
            pre[i] = p
            p *= nums[i]
        
        for i in reversed(range(len(nums))):
            pre[i] *= s
            s *= nums[i]
            
        return pre