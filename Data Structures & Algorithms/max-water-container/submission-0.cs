public class Solution {
    public int MaxArea(int[] heights) {
        int l = 0, r = heights.Length - 1, max = 0;

        while (l < r) {
            int left = heights[l], right = heights[r];
            int area = (r - l) * Math.Min(left, right);

            if (area > max) max = area;
            if (left < right) l++;
            else r--;
        }

        return max;
    }
}
