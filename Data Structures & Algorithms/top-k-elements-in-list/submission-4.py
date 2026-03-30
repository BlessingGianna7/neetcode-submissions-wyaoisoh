import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for n , freq in d.items():
            buckets[freq].append(n)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            if len(buckets[i]) > 0:
                for num in buckets[i]:
                  if len(res) < k:
                      res.append(num) 
        return res    