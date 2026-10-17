import java.util.Scanner;

class NumberException extends Exception {
    NumberException (String s) {
        super(s);
    }
}

class T {
    public static void main(String[] a) {
        Scanner s = new Scanner(System.in);
        try {
            System.out.print("Enter number: ");
            int n = s.nextInt();
            if (n == 0)
                throw new NumberException ("Number is 0");
            boolean p = true;
            if (n < 2)
                p = false;
            else {
                for (int i = 2; i <= n / 2; i++) {
                    if (n % i == 0) {
                        p = false;
                        break;
                    }
                }
            }
            if (p)
                System.out.println("Number is Prime");
            else
                System.out.println("Number is Not Prime");
        }
        catch (NumberException e) {
            System.out.println(e.getMessage());
        }
    }
}
