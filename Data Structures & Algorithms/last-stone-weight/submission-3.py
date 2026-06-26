class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        result = max_heap
        heapq.heapify(result)

        while len(result) > 1:
            a = abs(heapq.heappop(result))
            b = abs(heapq.heappop(result))

            if a == b:
                continue;
            elif a > b:
                c = a - b
                heapq.heappush(result, -c)
            else:
                c = b - a
                heapq.heappush(result, -c)

        if len(result) == 1:
            return abs(result[0])
        else:
            return 0    