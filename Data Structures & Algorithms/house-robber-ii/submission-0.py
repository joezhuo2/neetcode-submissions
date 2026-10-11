class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(start: int, end: int) -> int:
            prev1, prev2 = 0, 0
            for i in range(start, end + 1):
                prev1, prev2 = max(prev1, prev2 + nums[i]), prev1
            return prev1

        return max(rob_linear(0, len(nums) - 2), rob_linear(1, len(nums) - 1))