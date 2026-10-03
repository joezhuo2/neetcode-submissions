class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start: int, cur: List[int], sum: int):
            if sum == target:
                ans.append(list(cur))
                return
            if sum > target:
                return
            
            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(i, cur, sum + nums[i])
                cur.pop()

        backtrack(0, [], 0)
        return ans