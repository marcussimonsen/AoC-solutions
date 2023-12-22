package monkey;

public class LLQueue implements Queue {
    private class Node {
        public Node next;
        public int val;
        public Node(int val) {
            this.val = val;
        }
    }
    
    private Node first;

    public LLQueue() {

    }

    @Override
    public void enqueue(int i) {
        Node tmp = new Node(i);
        tmp.next = first;
        first = tmp;
    }

    @Override
    public int dequeue() {
        Node tmp = first;
        first = first.next;
        return tmp.val;
    }

    @Override
    public boolean isEmpty() {
        return first == null;
    }
}
