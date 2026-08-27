public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> n = new();
        for (int i = 0; i < nums.Count(); i++) {
            int cur = nums[i];
            int d = target - cur;
            if (n.ContainsKey(d)) {
                if (n[d] > i)  return new int[] {i, n[d]};
                else return new int[] {n[d], i};
            }
            n[cur] = i;
        }
        return new int[0];
    }
}
