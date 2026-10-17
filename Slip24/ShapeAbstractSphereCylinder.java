import java.util.Scanner;

abstract class Shape {
    abstract double area();
    abstract double volume();
}

class Sphere extends Shape {
    double r;

    Sphere(double r) {
        this.r = r;
    }

    double area() {
        return 4 * 3.14 * r * r;
    }

    double volume() {
        return (4.0 / 3) * 3.14 * r * r * r;
    }
}

class Cylinder extends Shape {
    double r, h;

    Cylinder(double r, double h) {
        this.r = r;
        this.h = h;
    }

    double area() {
        return 2 * 3.14 * r * (r + h);
    }

    double volume() {
        return 3.14 * r * r * h;
    }
}

public class ShapeAbstractSphereCylinder {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter radius of Sphere: ");
        Shape s = new Sphere(sc.nextDouble());
        System.out.print("Enter radius and height of Cylinder: ");
        Shape c = new Cylinder(sc.nextDouble(), sc.nextDouble());

        System.out.println("\nSphere   -> Area: " + s.area() + "  Volume: " + s.volume());
        System.out.println("Cylinder -> Area: " + c.area() + "  Volume: " + c.volume());
    }
}
