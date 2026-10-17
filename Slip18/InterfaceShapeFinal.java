import java.util.Scanner;

interface Shape {
    final double PI = 3.14;     // constant (final)
    void area();
}

class Circle implements Shape {
    final double r;

    Circle(double r) {
        this.r = r;
    }

    public void area() {
        System.out.println("Area of Circle = " + (PI * r * r));
    }
}

class Sphere implements Shape {
    final double r;

    Sphere(double r) {
        this.r = r;
    }

    public void area() {
        System.out.println("Area of Sphere = " + (4 * PI * r * r));
    }
}

public class InterfaceShapeFinal {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter radius of Circle: ");
        Shape c = new Circle(sc.nextDouble());
        System.out.print("Enter radius of Sphere: ");
        Shape s = new Sphere(sc.nextDouble());
        c.area();
        s.area();
    }
}
