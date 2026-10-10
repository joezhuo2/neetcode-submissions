class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        components = 0

        def dfs(node: int):
            visited[node] = True
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
                
        for i in range(n):
            if not visited[i]:
                components += 1
                dfs(i)
        
        return components