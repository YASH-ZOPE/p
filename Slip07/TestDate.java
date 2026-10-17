import java.util.Scanner;

class InvalidDateException extends Exception {
    InvalidDateException(String msg) {
        super(msg);
    }
}

class MyDate {
    int d, m, y;

    void accept() {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter date (dd mm yyyy): ");
        d = s.nextInt();
        m = s.nextInt();
        y = s.nextInt();
    }

    void display() {
        System.out.println("Date: " + d + "/" + m + "/" + y);
    }

    void check() throws InvalidDateException {
        int days;
        if (m < 1 || m > 12)
            throw new InvalidDateException("Invalid Date");
        if (m == 2) {
            if ((y % 400 == 0) || (y % 4 == 0 && y % 100 != 0))
                days = 29;
            else
                days = 28;
        }
        else if (m == 4 || m == 6 || m == 9 || m == 11)
            days = 30;
        else
            days = 31;
        if (d < 1 || d > days)
            throw new InvalidDateException("Invalid Date");
    }
}

public class TestDate {
    public static void main(String[] args) {
        MyDate x = new MyDate();
        try {
            x.accept();
            x.check();
            x.display();
        }
        catch (InvalidDateException e) {
            System.out.println(e.getMessage());
        }
    }
}
