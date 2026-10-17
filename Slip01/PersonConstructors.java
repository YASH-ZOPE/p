import java.util.Scanner;

class Person {
    int pid;
    String pname;
    int age;
    String gender;

    Person() {                      // default constructor
        this.pid = 0;
        this.pname = "Unknown";
        this.age = 0;
        this.gender = "Unknown";
    }

    Person(int pid, String pname) { // overloaded constructor
        this();
        this.pid = pid;
        this.pname = pname;
    }

    Person(int pid, String pname, int age, String gender) { // parameterized
        this.pid = pid;
        this.pname = pname;
        this.age = age;
        this.gender = gender;
    }

    void display() {
        System.out.println("ID: " + pid + "  Name: " + pname + "  Age: " + age + "  Gender: " + gender);
    }
}

public class PersonConstructors {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Person[] p = new Person[5];
        for (int i = 0; i < 5; i++) {
            System.out.println("\nEnter details of person " + (i + 1));
            System.out.print("ID: ");     int id = sc.nextInt();
            System.out.print("Name: ");   String nm = sc.next();
            System.out.print("Age: ");    int a = sc.nextInt();
            System.out.print("Gender: "); String g = sc.next();
            p[i] = new Person(id, nm, a, g);
        }
        System.out.println("\n--- Person Details ---");
        for (Person x : p) x.display();

        System.out.println("\n--- Default and overloaded constructor ---");
        new Person().display();
        new Person(99, "Test").display();
    }
}
