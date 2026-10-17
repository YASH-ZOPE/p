import java.util.*;

public class NegativeIntegersLinkedList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList<Integer> l = new LinkedList<>();
        System.out.print("Enter number of integers: ");
        int n = sc.nextInt();
        System.out.println("Enter integers:");
        for (int i = 0; i < n; i++)
            l.add(sc.nextInt());

        System.out.println("\nNegative integers:");
        for (int x : l)
            if (x < 0)
                System.out.println(x);
    }
}
