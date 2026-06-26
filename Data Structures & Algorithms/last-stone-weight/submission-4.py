class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            a = heapq.heappop(max_heap)
            b = heapq.heappop(max_heap)
            if b > a:
                heapq.heappush(max_heap, a - b)

        max_heap.append(0)
        return abs(max_heap[0])