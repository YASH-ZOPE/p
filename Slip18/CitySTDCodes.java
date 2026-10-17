import java.util.*;

public class CitySTDCodes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<String, String> map = new HashMap<>();   // keys are unique -> no duplicates
        map.put("Pune", "020");
        map.put("Mumbai", "022");
        map.put("Nashik", "0253");

        int ch;
        do {
            System.out.println("\n1. Add city and STD code\n2. Remove city\n3. Search city\n4. Display all\n5. Exit");
            System.out.print("Enter choice: ");
            ch = sc.nextInt();
            switch (ch) {
                case 1:
                    System.out.print("Enter city and STD code: ");
                    String city = sc.next(), code = sc.next();
                    if (map.containsKey(city))
                        System.out.println("City already exists (duplicates not allowed).");
                    else {
                        map.put(city, code);
                        System.out.println("City added.");
                    }
                    break;
                case 2:
                    System.out.print("Enter city to remove: ");
                    String r = sc.next();
                    if (map.remove(r) != null)
                        System.out.println("City removed.");
                    else
                        System.out.println("City not found.");
                    break;
                case 3:
                    System.out.print("Enter city to search: ");
                    String s = sc.next();
                    if (map.containsKey(s))
                        System.out.println("STD code of " + s + " = " + map.get(s));
                    else
                        System.out.println("City not found.");
                    break;
                case 4:
                    for (Map.Entry<String, String> e : map.entrySet())
                        System.out.println(e.getKey() + " : " + e.getValue());
                    break;
            }
        } while (ch != 5);
    }
}
