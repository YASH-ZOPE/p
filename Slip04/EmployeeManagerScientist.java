import java.util.Scanner;

class Employee {
    int empcode;
    String empname;

    void accept(Scanner sc) {
        System.out.print("Enter empcode and empname: ");
        empcode = sc.nextInt();
        empname = sc.next();
    }

    void display() {
        System.out.println("Emp Code: " + empcode + "  Name: " + empname);
    }
}

class Manager extends Employee {
    String designation;
    double clubDues;

    void accept(Scanner sc) {
        super.accept(sc);
        System.out.print("Enter designation and club dues: ");
        designation = sc.next();
        clubDues = sc.nextDouble();
    }

    void display() {
        super.display();
        System.out.println("Designation: " + designation + "  Club Dues: " + clubDues);
    }
}

class Scientist extends Employee {
    String deptname;
    int publications;

    void accept(Scanner sc) {
        super.accept(sc);
        System.out.print("Enter department name and publications: ");
        deptname = sc.next();
        publications = sc.nextInt();
    }

    void display() {
        super.display();
        System.out.println("Department: " + deptname + "  Publications: " + publications);
    }
}

public class EmployeeManagerScientist {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of employees: ");
        int n = sc.nextInt();
        Employee[] e = new Employee[n];
        for (int i = 0; i < n; i++) {
            System.out.print("\n1. Manager  2. Scientist - choose type: ");
            int ch = sc.nextInt();
            e[i] = (ch == 1) ? new Manager() : new Scientist();
            e[i].accept(sc);
        }
        System.out.println("\n--- Employee Information ---");
        for (Employee x : e) {
            x.display();
            System.out.println();
        }
    }
}
