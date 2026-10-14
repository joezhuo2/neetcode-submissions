class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        p1, p2 = 1, 1

        for i in range(1, len(s)):
            cur = 0

            if s[i] != '0':
                cur += p1
            
            two_dig = int(s[i-1:i+1])
            if 10 <= two_dig <= 26:
                cur += p2

            p2 = p1
            p1 = cur
        
        return p1