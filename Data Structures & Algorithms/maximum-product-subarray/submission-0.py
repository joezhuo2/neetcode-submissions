class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        g_max = c_max = c_min = nums[0]

        for n in nums[1:]:
            if n < 0:
                c_max, c_min = c_min, c_max
            
            c_max = max(n, c_max * n)
            c_min = min(n, c_min * n)

            g_max = max(g_max, c_max)

        return g_max