class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = {c for w in words for c in w}
        adj, in_deg = {c: set() for c in chars}, {c: 0 for c in chars}
        
        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1[:len(w2)] == w2: return ""
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_deg[c2] += 1
                    break
                    
        q = deque([c for c, d in in_deg.items() if d == 0])
        res = []
        
        while q:
            res.append(c := q.popleft())
            for n in adj[c]:
                in_deg[n] -= 1
                if in_deg[n] == 0: q.append(n)
                
        return "".join(res) if len(res) == len(chars) else ""