class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        area = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0,-1]]
        rows , cols = len(grid) , len(grid[0])

        def dfs(r, c):
            if (r,c) in visited or r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            
            return 1 + sum(dfs(r + dr, c + dc) for dr, dc in directions)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    a = dfs(r, c)
                    area = max(area, a)
                    visited.add((r,c))

        return area