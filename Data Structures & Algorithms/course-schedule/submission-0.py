class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degree = [0] * numCourses

        for c, p in prerequisites:
            adj[p].append(c)
            in_degree[c] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        processed_count = 0

        while queue:
            cur = queue.popleft()
            processed_count += 1

            for n in adj[cur]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    queue.append(n)

        return processed_count == numCourses