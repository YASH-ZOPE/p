import java.util.*;

class City {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        ArrayList<String> a = new ArrayList<>();

        System.out.print("Enter number of cities: ");
        int n = s.nextInt();

        System.out.println("Enter city names:");
        for (int i = 0; i < n; i++) {
            a.add(s.next());
        }

        System.out.println("\nCity List:");
        System.out.println(a);

        a.clear();

        System.out.println("\nAfter removing all elements:");
        System.out.println(a);
    }
}
