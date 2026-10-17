import java.util.*;

class ColorList {
    public static void main(String[] args) {
        LinkedList<String> l = new LinkedList<>();

        l.add("Red");
        l.add("Blue");
        l.add("Yellow");
        l.add("Orange");

        System.out.println("List using Iterator:");
        Iterator<String> i = l.iterator();
        while (i.hasNext()) {
            System.out.println(i.next());
        }

        System.out.println("\nList in Reverse Order:");
        ListIterator<String> li = l.listIterator(l.size());
        while (li.hasPrevious()) {
            System.out.println(li.previous());
        }

        LinkedList<String> l2 = new LinkedList<>();
        l2.add("Pink");
        l2.add("Green");

        l.addAll(2, l2);

        System.out.println("\nFinal List:");
        System.out.println(l);
    }
}
