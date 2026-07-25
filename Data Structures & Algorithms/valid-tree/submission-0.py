class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        visited = set()
        tree = {i: [] for i in range(n)}
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
    
        def dfs(child, p):
            if child in visited:
                return False

            visited.add(child)
            for c in tree[child]:
                if c == p:
                    continue
                if not dfs(c, child):   
                    return False
            return True     

        return dfs(0, -1) and n == len(visited)