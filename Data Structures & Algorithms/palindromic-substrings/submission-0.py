class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        ans = 0

        def expand_around_center(l: int, r: int):
            nonlocal ans;
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            expand_around_center(i, i)
            expand_around_center(i, i+1)

        return ans


