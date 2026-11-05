class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = {0: 1}
        cur = 0
        count = 0

        for n in nums:
            cur += n

            target = cur - k

            if target in prefix_counts:
                count += prefix_counts[target]

            prefix_counts[cur] = prefix_counts.get(cur, 0) + 1
        
        return count