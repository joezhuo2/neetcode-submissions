class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            n = root
            for c in w:
                if c not in n.children:
                    n.children[c] = TrieNode()
                n = n.children[c]
            n.word = w
        
        rows, cols = len(board), len(board[0])
        ans = []

        def dfs(r, c, n):
            char = board[r][c]
            cur = n.children[char]

            if cur.word:
                ans.append(cur.word)
                cur.word = None

            board[r][c] = '#'

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in cur.children:
                    dfs(nr, nc, cur)
            
            board[r][c] = char

            if not cur.children:
                n.children.pop(char)
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        
        return ans
