import java.util.Scanner;

class Student {
    int rollno;
    String name;
    double percentage;

    Student() {                                  // default constructor
        this.rollno = 0;
        this.name = "Unknown";
        this.percentage = 0.0;
    }

    Student(int rollno, String name) {           // overloaded constructor
        this();
        this.rollno = rollno;
        this.name = name;
    }

    Student(int rollno, String name, double percentage) {  // parameterized
        this.rollno = rollno;
        this.name = name;
        this.percentage = percentage;
    }

    void display() {
        System.out.println("Roll No: " + rollno + "  Name: " + name + "  Percentage: " + percentage);
    }
}

public class StudentThis {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Student[] s = new Student[5];
        for (int i = 0; i < 5; i++) {
            System.out.print("Enter rollno, name, percentage of student " + (i + 1) + ": ");
            s[i] = new Student(sc.nextInt(), sc.next(), sc.nextDouble());
        }
        System.out.println("\n--- Student Details ---");
        for (Student x : s) x.display();

        System.out.println("\n--- Default and overloaded constructor ---");
        new Student().display();
        new Student(1, "Test").display();
    }
}
