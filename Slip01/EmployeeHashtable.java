import java.util.*;

class Employee {
    public static void main(String[] args) {
        Hashtable<String, Double> ht = new Hashtable<>();

        ht.put("Amit", 25000.0);
        ht.put("Priya", 30000.0);
        ht.put("Rahul", 28000.0);
        ht.put("Sneha", 35000.0);

        System.out.println("Employee Details:");
        for (Map.Entry<String, Double> e : ht.entrySet()) {
            System.out.println("Name: " + e.getKey() + "  Salary: " + e.getValue());
        }

        String n = "Priya";

        if (ht.containsKey(n)) {
            System.out.println("\nEmployee: " + n);
            System.out.println("Salary: " + ht.get(n));
        } else {
            System.out.println("\nEmployee not found.");
        }
    }
}
