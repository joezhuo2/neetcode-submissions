public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int[] sol = new int[nums.Length];
        int p = 1;
        for (int i = 0; i < nums.Length; i++) {
            sol[i] = p;
            p *= nums[i];
        }
        int s = 1;
        for (int i = nums.Length - 1; i >= 0; i--) {
            sol[i] *= s;
            s *= nums[i];
        }
        return sol;
    }
}
