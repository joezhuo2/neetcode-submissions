public class Solution {
    public bool IsValidSudoku(char[][] board) {
        var seen = new HashSet<string>();

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char val = board[r][c];

                if (val == '.') continue;

                if (!seen.Add($"{val} in r{r}") || 
                    !seen.Add($"{val} in c{c}") || 
                    !seen.Add($"{val} in b{(r/3) * 3 + (c/3)}"))
                    return false;
            }
        }

        return true;
    }
}
