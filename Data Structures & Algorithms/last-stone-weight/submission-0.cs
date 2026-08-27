public class Solution {
    public int LastStoneWeight(int[] stones) {
        var maxHeap = new PriorityQueue<int, int>();

        foreach (int s in stones) maxHeap.Enqueue(s, -s);

        while (maxHeap.Count > 1) {
            int y = maxHeap.Dequeue();
            int x = maxHeap.Dequeue();

            if (x != y) {
                int r = y - x;
                maxHeap.Enqueue(r, -r);
            }
        }
        return maxHeap.Count == 1 ? maxHeap.Dequeue() : 0;
    }
}
