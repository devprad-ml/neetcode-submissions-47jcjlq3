class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()

        for i, n in enumerate(nums):
            comp = target - n

            if comp in map:
                return [map[comp], i]
            
            map[n] = i
        return None
            
        