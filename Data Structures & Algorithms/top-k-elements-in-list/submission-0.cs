public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> count = new();
        foreach (int i in nums) {
            if (count.ContainsKey(i)) count[i]++;
            else count.Add(i, 1);
        }
        return count.OrderByDescending(kvp => kvp.Value).Take(k).Select(kvp => kvp.Key).ToArray();
    }
}
