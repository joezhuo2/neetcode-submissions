class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parent = list(range(n))

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i: int, j: int) -> bool:
            ri = find(i)
            rj = find(j)

            if ri == rj:
                return False
            
            parent[ri] = rj
            return True

        for u, v in edges:
            if not union(u, v):
                return False
            
        return True