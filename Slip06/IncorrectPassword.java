import java.util.Scanner;

class IncorrectPasswordException extends Exception {
    IncorrectPasswordException(String msg) {
        super(msg);
    }
}

public class IncorrectPassword {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.print("Enter username: ");
            String user = sc.next();
            System.out.print("Enter password: ");
            String pass = sc.next();
            if (!user.equals(pass))
                throw new IncorrectPasswordException("Incorrect Password Exception");
            System.out.println("Login successful");
        } catch (IncorrectPasswordException e) {
            System.out.println(e.getMessage());
        }
    }
}
