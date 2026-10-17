import java.util.Scanner;

class Employee {
    int id;
    String name;
    double salary;

    Employee(int id, String name, double salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }
}

public class EmployeeMaxSalary {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of employees: ");
        int n = sc.nextInt();
        Employee[] e = new Employee[n];
        for (int i = 0; i < n; i++) {
            System.out.print("Enter id, name, salary of employee " + (i + 1) + ": ");
            e[i] = new Employee(sc.nextInt(), sc.next(), sc.nextDouble());
        }
        int max = 0;
        for (int i = 1; i < n; i++)
            if (e[i].salary > e[max].salary) max = i;
        System.out.println("\nEmployee with maximum salary: " + e[max].name + " (Salary = " + e[max].salary + ")");
    }
}
