class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        ans = []

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        for k, v in count.items():
            if v > len(nums)//3:
                ans.append(k)
            
        return ans