class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for c in intervals[1:]:
            p = merged[-1]

            if c[0] <= p[1]:
                p[1] = max(p[1], c[1])
            else:
                merged.append(c)
        return merged