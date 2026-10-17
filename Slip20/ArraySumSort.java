import java.util.*;

public class ArraySumSort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();
        int[] a = new int[n];
        int sum = 0;
        System.out.println("Enter elements:");
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
            sum += a[i];
        }
        System.out.println("Sum of elements = " + sum);
        Arrays.sort(a);
        System.out.println("Array in ascending order: " + Arrays.toString(a));
    }
}
