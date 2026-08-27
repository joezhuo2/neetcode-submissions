public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> found = new();
        for (int i = 0; i < nums.Count(); i++) {
            if (found.Count > 0 && found.Contains(nums[i])) return true;
            found.Add(nums[i]); 
        }
        return false;
    }
}