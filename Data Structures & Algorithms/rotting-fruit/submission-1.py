class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # seed the queue with all initially rotten oranges, count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0  # nothing to rot, 0 minutes needed

        time = 0
        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):  # process one full minute/level at a time
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))

        return time if fresh == 0 else -1