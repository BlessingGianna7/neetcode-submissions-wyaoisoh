import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-x for x in counts.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = collections.deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                a = heapq.heappop(maxHeap)
                a += 1
                if a != 0:
                    q.append([a, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time