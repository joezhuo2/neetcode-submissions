class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx = 0 
        merged = []

        while idx < len(word1) and idx < len(word2):
            merged.append(word1[idx])
            merged.append(word2[idx])
            idx += 1
        
        merged.append(word1[idx:])
        merged.append(word2[idx:])

        return "".join(merged)