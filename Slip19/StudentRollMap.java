import java.util.*;

public class StudentRollMap {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<String, java.lang.Integer> map = new HashMap<>();   // unique student names
        map.put("Amit", 1);
        map.put("Priya", 2);
        map.put("Rahul", 3);

        int ch;
        do {
            System.out.println("\n1. Add student and roll number\n2. Remove student\n3. Search student\n4. Display all\n5. Exit");
            System.out.print("Enter choice: ");
            ch = sc.nextInt();
            switch (ch) {
                case 1:
                    System.out.print("Enter student name and roll number: ");
                    String name = sc.next();
                    int roll = sc.nextInt();
                    if (map.containsKey(name))
                        System.out.println("Student already exists (duplicates not allowed).");
                    else {
                        map.put(name, roll);
                        System.out.println("Student added.");
                    }
                    break;
                case 2:
                    System.out.print("Enter student name to remove: ");
                    if (map.remove(sc.next()) != null)
                        System.out.println("Student removed.");
                    else
                        System.out.println("Student not found.");
                    break;
                case 3:
                    System.out.print("Enter student name to search: ");
                    String s = sc.next();
                    if (map.containsKey(s))
                        System.out.println("Roll number of " + s + " = " + map.get(s));
                    else
                        System.out.println("Student not found.");
                    break;
                case 4:
                    for (Map.Entry<String, java.lang.Integer> e : map.entrySet())
                        System.out.println(e.getKey() + " : " + e.getValue());
                    break;
            }
        } while (ch != 5);
    }
}
