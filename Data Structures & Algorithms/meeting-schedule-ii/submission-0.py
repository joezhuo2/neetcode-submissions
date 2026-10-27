"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        free = []

        heapq.heappush(free, intervals[0].end)

        for i in intervals[1:]:
            if free[0] <= i.start:
                heapq.heappop(free)

            heapq.heappush(free, i.end)
        
        return len(free)
