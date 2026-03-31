import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        we need to return top k frequent elements
        "frequent" hints us towards a hashmap or a key: val data struct
        the top K hints us towards a heap. Py has only min heap so we can use 
        that to our advantage.
        """
        # init Counter
        count = Counter(nums)
        # init heap
        heap = []

        # go thru counter and append tuple of (freq, num)
        for n, c in count.items():
            heapq.heappush(heap, (c, n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [n for c, n in heap]
        