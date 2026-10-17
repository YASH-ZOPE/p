import java.util.*;

public class LinkedHashSetDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedHashSet<String> set = new LinkedHashSet<>();
        System.out.print("Enter number of items: ");
        int n = sc.nextInt();
        System.out.println("Enter data:");
        for (int i = 0; i < n; i++)
            set.add(sc.next());

        System.out.println("\nContents (insertion order, duplicates removed):");
        Iterator<String> it = set.iterator();
        while (it.hasNext())
            System.out.println(it.next());
    }
}
