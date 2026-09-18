class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        _dict = defaultdict(int)

        for n in nums:
            _dict[n] += 1
        
        majority_threshold = len(nums) // 2
        for k, v in _dict.items():
            if v > majority_threshold:
                return k
            
        
