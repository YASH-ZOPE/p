import java.util.*;

public class TreeSetColors {
    public static void main(String[] args) {
        TreeSet<String> t = new TreeSet<>();
        t.add("Red");
        t.add("Green");
        t.add("Blue");
        t.add("Yellow");
        t.add("Orange");
        System.out.println("TreeSet in ascending order:");
        for (String c : t)
            System.out.println(c);
    }
}
