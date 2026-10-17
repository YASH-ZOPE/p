import java.util.*;

class Num {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        TreeSet<Integer> t = new TreeSet<>();

        System.out.print("Enter number of integers: ");
        int n = s.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.print("Enter number: ");
            t.add(s.nextInt());
        }

        System.out.println("\nSorted Elements:");
        System.out.println(t);

        System.out.print("\nEnter element to search: ");
        int x = s.nextInt();

        if (t.contains(x))
            System.out.println("Element found");
        else
            System.out.println("Element not found");
    }
}
