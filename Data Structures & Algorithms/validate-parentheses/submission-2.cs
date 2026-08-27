public class Solution {
    public bool IsValid(string s) {
        Dictionary<char, char> m = new() {{')', '('}, {'}', '{'}, {']', '['}};
        Stack<char> st = new();
        foreach (char c in s) {
            if (m.ContainsKey(c)) {
                if (st.Count == 0 || st.Pop() != m[c]) return false;
            }
            else {
                st.Push(c);
            }
        }
        return st.Count == 0;
    }
}
