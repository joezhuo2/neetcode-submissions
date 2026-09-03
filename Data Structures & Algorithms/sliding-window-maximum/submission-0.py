class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        indexes = deque()

        sol = []

        for i, n in enumerate(nums):
            while indexes and nums[indexes[-1]] <= n:
                indexes.pop()
            indexes.append(i)

            if indexes[0] <= i - k:
                indexes.popleft()
            
            if i >= k - 1:
                sol.append(nums[indexes[0]]);
        
        return sol