import strings.Con;
import strings.Comp;
import java.util.Scanner;

public class StringOpsDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first string: ");
        String a = sc.next();
        System.out.print("Enter second string: ");
        String b = sc.next();

        Con c = new Con();
        Comp m = new Comp();
        System.out.println("Concatenated string: " + c.concat(a, b));
        if (m.compare(a, b))
            System.out.println("Both strings are equal");
        else
            System.out.println("Strings are not equal");
    }
}
