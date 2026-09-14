class MedianFinder:

    def __init__(self):
        self._maxHeap = []
        self._minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self._maxHeap, -num)

        if self._maxHeap and self._minHeap and (-self._maxHeap[0] > self._minHeap[0]):
            val = -heapq.heappop(self._maxHeap)
            heapq.heappush(self._minHeap, val)
        
        if len(self._maxHeap) > len(self._minHeap) + 1:
            val = -heapq.heappop(self._maxHeap)
            heapq.heappush(self._minHeap, val)
        elif len(self._minHeap) > len(self._maxHeap):
            val = heapq.heappop(self._minHeap)
            heapq.heappush(self._maxHeap, -val)

    def findMedian(self) -> float:
        return float(-self._maxHeap[0]) if len(self._maxHeap) > len(self._minHeap) else float(-self._maxHeap[0] + self._minHeap[0]) / 2.0
