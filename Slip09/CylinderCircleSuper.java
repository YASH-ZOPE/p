import java.util.Scanner;

class Circle {
    double r;
    Circle(double r) {
        this.r = r;
    }
    void area() {
        System.out.println("Area of Circle = " + (3.14 * r * r));
    }
}

class Cylinder extends Circle {
    double h;
    Cylinder(double r, double h) {
        super(r);
        this.h = h;
    }
    void area() {
        System.out.println("Area of Cylinder = " + (2 * 3.14 * super.r * (super.r + h)));
    }
}

class Demo {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Radius: ");
        double r = sc.nextDouble();
        System.out.print("Enter Height: ");
        double h = sc.nextDouble();
        Circle c = new Circle(r);
        Cylinder cy = new Cylinder(r, h);
        c.area();
        cy.area();
    }
}
