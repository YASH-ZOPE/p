class RollnoException extends Exception {
    RollnoException(String msg) {
        super(msg);
    }
}

class Student {
    int roll, age;
    String name, course;

    Student(int r, String n, int a, String c) throws RollnoException {
        if (r < 13001 || r > 13080)
            throw new RollnoException("Rollno Not Within The Range");
        roll = r;
        name = n;
        age = a;
        course = c;
    }

    void display() {
        System.out.println("Roll No: " + roll);
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Course: " + course);
    }
}

public class StudentRollRangeException {
    public static void main(String[] args) {
        try {
            Student s1 = new Student(13010, "Rahul", 18, "BCA");
            s1.display();
            Student s2 = new Student(13100, "Amit", 19, "BCA");   // invalid
            s2.display();
        } catch (RollnoException e) {
            System.out.println(e.getMessage());
        }
    }
}
