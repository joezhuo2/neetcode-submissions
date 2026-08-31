public class Solution {
    public int CharacterReplacement(string s, int k) {
        int[] count = new int[26];
        int l = 0;
        int maxFreq = 0;
        int maxLength = 0;

        for (int r = 0; r < s.Length; r++) {
            count[s[r] - 'A']++;

            maxFreq = Math.Max(maxFreq, count[s[r] - 'A']);

            while (r - l + 1 - maxFreq > k) {
                count[s[l] - 'A']--;
                l++;
            }

            maxLength = Math.Max(maxLength, r - l + 1);
        }

        return maxLength;
    }
}
