public class Solution {
    public bool IsAnagram(string s, string t) {
        int l = s.Length;
        int n = t.Length;
        if (n != l) return false;
        int[] counts = new int[26];
        for (int i = 0; i < l; i++) {
            counts[s[i] - 'a']++;
            counts[t[i] - 'a']--;
        }
        for (int i = 0; i < counts.Length; i++) {
            if (counts[i] != 0) return false;
        }
        return true;
    }
}
