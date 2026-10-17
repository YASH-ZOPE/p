import java.util.Scanner;

class Vehicle {
    String company;
    double price;

    Vehicle(String company, double price) {
        this.company = company;
        this.price = price;
    }

    void display() {
        System.out.println("Company: " + company + "  Price: " + price);
    }
}

class LightMotorVehicle extends Vehicle {
    double mileage;

    LightMotorVehicle(String company, double price, double mileage) {
        super(company, price);
        this.mileage = mileage;
    }

    void display() {
        System.out.print("[Light Motor Vehicle] ");
        super.display();
        System.out.println("Mileage: " + mileage + " km/l");
    }
}

class HeavyMotorVehicle extends Vehicle {
    double capacity;

    HeavyMotorVehicle(String company, double price, double capacity) {
        super(company, price);
        this.capacity = capacity;
    }

    void display() {
        System.out.print("[Heavy Motor Vehicle] ");
        super.display();
        System.out.println("Capacity: " + capacity + " tons");
    }
}

public class VehicleInheritance {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of vehicles: ");
        int n = sc.nextInt();
        Vehicle[] v = new Vehicle[n];
        for (int i = 0; i < n; i++) {
            System.out.print("\n1. Light Motor Vehicle  2. Heavy Motor Vehicle - choose type: ");
            int ch = sc.nextInt();
            System.out.print("Enter company and price: ");
            String c = sc.next();
            double p = sc.nextDouble();
            if (ch == 1) {
                System.out.print("Enter mileage: ");
                v[i] = new LightMotorVehicle(c, p, sc.nextDouble());
            } else {
                System.out.print("Enter capacity in tons: ");
                v[i] = new HeavyMotorVehicle(c, p, sc.nextDouble());
            }
        }
        System.out.println("\n--- Vehicle Information ---");
        for (Vehicle x : v) x.display();
    }
}
