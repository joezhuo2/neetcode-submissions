class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heap = []

        for i in points:
            heapq.heappush(heap, (self.dist(i[0], i[1]), i))

        while k > 0:
            dist, pt = heapq.heappop(heap)
            ans.append(pt)
            k -= 1
        
        return ans
        
    def dist(self, x2: int, y2: int) -> float:
        return math.hypot(x2, y2)