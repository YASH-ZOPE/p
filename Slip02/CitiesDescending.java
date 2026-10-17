import java.util.*;

public class CitiesDescending {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of cities: ");
        int n = sc.nextInt();
        ArrayList<String> cities = new ArrayList<>();
        System.out.println("Enter city names:");
        for (int i = 0; i < n; i++) cities.add(sc.next());

        Collections.sort(cities, Collections.reverseOrder());
        System.out.println("\nCities in descending order:");
        for (String c : cities) System.out.println(c);
    }
}
