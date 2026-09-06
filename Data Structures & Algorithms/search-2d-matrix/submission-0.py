class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        t, b = 0, len(matrix) - 1
        row = -1

        while t <= b:
            m = t + (b - t) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:
                row = m
                break
            elif matrix[m][0] < target:
                t = m + 1
            else:
                b = m - 1
        if row == -1:
            return False

        return self.bfs(matrix[row], target)

    def bfs(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False