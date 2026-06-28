class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for x in nums:
            res.append(-x)

        heapq.heapify(res)
        for _ in range(k - 1):
            heapq.heappop(res)    

        return -res[0]