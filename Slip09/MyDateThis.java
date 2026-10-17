import java.util.Scanner;

class MyDate {
    int dd, mm, yy;

    MyDate() {
        this.dd = 1;
        this.mm = 1;
        this.yy = 2000;
    }

    MyDate(int dd, int mm, int yy) {
        this.dd = dd;
        this.mm = mm;
        this.yy = yy;
    }

    void display() {
        System.out.println("Date: " + this.dd + "-" + this.mm + "-" + this.yy);
    }
}

public class MyDateThis {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter dd mm yy: ");
        MyDate d1 = new MyDate(sc.nextInt(), sc.nextInt(), sc.nextInt());
        MyDate d2 = new MyDate();
        d1.display();
        d2.display();
    }
}
