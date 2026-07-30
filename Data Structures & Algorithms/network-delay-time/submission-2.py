class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]
        visited = set()
        maxTime = 0

        while heap:
            dist, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            maxTime = dist

            for nei, weight in graph[node]:
                if nei not in visited:
                    heapq.heappush(heap, (dist + weight, nei))

        if len(visited) == n:
            return maxTime
        return -1