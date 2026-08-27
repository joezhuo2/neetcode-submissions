public class Solution {
    public int LongestConsecutive(int[] nums) {
        HashSet<int> set = new(nums);
        int longest = 0;
        foreach(int i in nums) {
            if (!set.Contains(i - 1)) {
                int l = 1;
                int cur = i;
                while (set.Contains(cur + 1)) {
                    cur++;
                    l++;
                }

                longest = Math.Max(longest, l);
            }
        }
        return longest;
    }
}
