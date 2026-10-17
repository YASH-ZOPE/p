import java.util.Scanner;

abstract class Staff {
    String name, address;

    Staff(String name, String address) {
        this.name = name;
        this.address = address;
    }

    abstract double calculateSalary();
}

class FullTimeStaff extends Staff {
    String department;
    double salary, hra, da;

    FullTimeStaff(String name, String address, String department, double salary) {
        super(name, address);
        this.department = department;
        this.salary = salary;
        this.hra = 0.08 * salary;
        this.da = 0.05 * salary;
    }

    double calculateSalary() {
        return salary + hra + da;
    }

    void display() {
        System.out.println("Name: " + name + "  Address: " + address + "  Dept: " + department);
        System.out.println("Basic: " + salary + "  HRA: " + hra + "  DA: " + da);
        System.out.println("Total Salary: " + calculateSalary());
    }
}

class PartTimeStaff extends Staff {
    int hours;
    double rate;

    PartTimeStaff(String name, String address, int hours, double rate) {
        super(name, address);
        this.hours = hours;
        this.rate = rate;
    }

    double calculateSalary() {
        return hours * rate;
    }

    void display() {
        System.out.println("Name: " + name + "  Address: " + address);
        System.out.println("Hours: " + hours + "  Rate/hour: " + rate);
        System.out.println("Total Salary: " + calculateSalary());
    }
}

public class StaffAbstract {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of staff: ");
        int n = sc.nextInt();
        Staff[] s = new Staff[n];
        for (int i = 0; i < n; i++) {
            System.out.print("\n1. Full Time  2. Part Time - choose: ");
            int ch = sc.nextInt();
            System.out.print("Enter name and address: ");
            String nm = sc.next(), ad = sc.next();
            if (ch == 1) {
                System.out.print("Enter department and salary: ");
                s[i] = new FullTimeStaff(nm, ad, sc.next(), sc.nextDouble());
            } else {
                System.out.print("Enter number of hours and rate per hour: ");
                s[i] = new PartTimeStaff(nm, ad, sc.nextInt(), sc.nextDouble());
            }
        }
        System.out.println("\n===== Full Time Staff =====");
        for (Staff x : s)
            if (x instanceof FullTimeStaff) { ((FullTimeStaff) x).display(); System.out.println(); }
        System.out.println("===== Part Time Staff =====");
        for (Staff x : s)
            if (x instanceof PartTimeStaff) { ((PartTimeStaff) x).display(); System.out.println(); }
    }
}
