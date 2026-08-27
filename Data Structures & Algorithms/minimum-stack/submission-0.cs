public class MinStack {
    Stack<int> s;
    Stack<int> min;
    
    public MinStack() {
        s = new();
        min = new();
    }
    
    public void Push(int val) {
        s.Push(val);
        min.Push(min.Count == 0 ? val : Math.Min(min.Peek(), val));
    }
    
    public void Pop() {
        s.Pop();
        min.Pop();
    }
    
    public int Top() {
        return s.Peek();
    }
    
    public int GetMin() {
        return min.Peek();
    }
}
