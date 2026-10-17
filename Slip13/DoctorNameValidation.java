import java.util.Scanner;

class InvalidNameException extends Exception {
    InvalidNameException(String s) {
        super(s);
    }
}

class TestName {
    public static void main(String[] a) {
        Scanner s = new Scanner(System.in);
        try {
            System.out.print("Enter Doctor Name: ");
            String n = s.nextLine();
            if (!n.matches("[a-zA-Z ]+"))
                throw new InvalidNameException("Name is Invalid");
            System.out.println("Doctor Name: " + n);
        }
        catch (InvalidNameException e) {
            System.out.println(e.getMessage());
        }
    }
}
