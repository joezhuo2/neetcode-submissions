public class Solution {
    public bool IsHappy(int n) {
        HashSet<int> seen = new();

        while (n != 1 && seen.Add(n)) {
            int sum = 0;
            while (n > 0) {
                int d = n % 10;
                sum += d * d;
                n /= 10;
            }
            n = sum;
        }
        return n == 1;
    }
}
