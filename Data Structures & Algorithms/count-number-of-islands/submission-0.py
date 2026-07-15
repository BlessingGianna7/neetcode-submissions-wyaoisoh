class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        rows , cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))

            while q :
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if(nr >= 0 and nc >= 0 and
                        nr < rows and nc < cols and
                         (nr,nc ) not in visited and grid[nr][nc] == "1"):

                            visited.add((nr, nc))
                            q.append((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0":
                    continue
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r,c)
                    islands += 1
                    visited.add((r, c))

        return islands