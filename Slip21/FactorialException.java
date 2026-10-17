import java.util.Scanner;

class NumberException extends Exception {
    NumberException(String s) {
        super(s);
    }
}

public class FactorialException {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        try {
            System.out.print("Enter number: ");
            int n = s.nextInt();
            if (n == 0)
                throw new NumberException("Number is 0");
            long f = 1;
            for (int i = 2; i <= n; i++)
                f *= i;
            System.out.println("Factorial of " + n + " = " + f);
        } catch (NumberException e) {
            System.out.println(e.getMessage());
        }
    }
}
