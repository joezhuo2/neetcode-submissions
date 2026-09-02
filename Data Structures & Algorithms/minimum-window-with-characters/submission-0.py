class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for c in t:
            freq[c] = freq.get(c, 0) + 1
        
        window = {}
        l, r = 0, 0
        need, have = len(freq), 0
        min_len = float("inf")
        best = [-1, -1]

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in freq and window[c] == freq[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < min_len:
                    best = [l, r]
                    min_len = r - l + 1
                
                left = s[l]
                window[left] -= 1
                if left in freq and window[left] < freq[left]:
                    have -= 1
                
                l += 1
        if min_len == float("inf"):
            return ""

        start, end = best
        return s[start : end + 1] 