import java.util.*;

public class StudentNamesIterator {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java StudentNamesIterator name1 name2 name3 ...");
            return;
        }
        ArrayList<String> list = new ArrayList<>();
        for (String s : args)
            list.add(s);

        System.out.println("Using Iterator (forward):");
        Iterator<String> it = list.iterator();
        while (it.hasNext())
            System.out.println(it.next());

        System.out.println("\nUsing ListIterator (forward then backward):");
        ListIterator<String> li = list.listIterator();
        while (li.hasNext())
            System.out.println(li.next());
        System.out.println("-- backward --");
        while (li.hasPrevious())
            System.out.println(li.previous());
    }
}
