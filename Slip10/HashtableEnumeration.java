import java.util.*;

public class HashtableEnumeration {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Hashtable<String, String> ht = new Hashtable<>();
        System.out.print("Enter number of students: ");
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.print("Enter mobile number and student name: ");
            String mobile = sc.next();
            String name = sc.next();
            ht.put(mobile, name);
        }
        System.out.println("\nStudent Details:");
        Enumeration<String> keys = ht.keys();
        while (keys.hasMoreElements()) {
            String k = keys.nextElement();
            System.out.println("Mobile: " + k + "  Name: " + ht.get(k));
        }
    }
}
