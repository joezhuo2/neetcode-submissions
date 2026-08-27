public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int l = 0, r = numbers.Length - 1;
        while (l < r) {
            int s = numbers[l] + numbers[r];
            if (s == target) return new int[] {l+1, r+1};

            if (s > target) r--;
            else l++;
        }
        return new int[0];
    }
}
