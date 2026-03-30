class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        heap = []
        for num, freq in d.items():
            heapq.heappush(heap, (-freq, num))  # negate for max heap

        res = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        return res