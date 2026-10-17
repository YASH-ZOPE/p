import java.util.*;

class SortMap {
    public static void main(String[] args) {
        HashMap<Integer, String> h = new HashMap<>();

        h.put(30, "Pune");
        h.put(10, "Mumbai");
        h.put(40, "Delhi");
        h.put(20, "Nashik");

        System.out.println("Before Sorting:");
        System.out.println(h);

        TreeMap<Integer, String> t = new TreeMap<>(h);

        System.out.println("\nAfter Sorting by Keys:");
        System.out.println(t);
    }
}
