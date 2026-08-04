class Solution:  
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        for s, d, price in flights:
            adj[s].append((d, price))

        heap = [(0, src, 0)]
        visited = {}  # node → fewest stops used to reach it

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost

            if stops > k:
                continue

            # only skip if we've been here with fewer or equal stops
            if node in visited and visited[node] <= stops:
                continue
            visited[node] = stops

            for nei, price in adj[node]:
                heapq.heappush(heap, (cost + price, nei, stops + 1))

        return -1