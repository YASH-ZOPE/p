import java.util.*;

public class SubjectsLinkedList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList<String> l = new LinkedList<>();
        System.out.print("Enter number of subjects: ");
        int n = sc.nextInt();
        System.out.println("Enter subject names:");
        for (int i = 0; i < n; i++)
            l.add(sc.next());

        System.out.println("\nSubjects:");
        Iterator<String> it = l.iterator();
        while (it.hasNext())
            System.out.println(it.next());
    }
}
