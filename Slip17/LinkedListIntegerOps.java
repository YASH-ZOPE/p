import java.util.*;

class IntList {
    public static void main(String[] args) {
        LinkedList<Integer> l = new LinkedList<>();

        l.add(10);
        l.add(20);
        l.add(30);

        System.out.println("Original List: " + l);

        l.addFirst(5);
        System.out.println("After adding at first: " + l);

        l.removeLast();
        System.out.println("After deleting last: " + l);

        System.out.println("Size of List: " + l.size());
    }
}
