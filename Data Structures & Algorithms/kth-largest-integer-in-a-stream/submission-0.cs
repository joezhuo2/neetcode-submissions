public class KthLargest {
    int _k;
    PriorityQueue<int, int> heap;

    public KthLargest(int k, int[] nums) {
        _k = k;
        heap = new();
        foreach (int n in nums) Add(n);
    }
    
    public int Add(int val) {
        heap.Enqueue(val, val);
        if (heap.Count > _k) heap.Dequeue();

        return heap.Peek();
    }
}
