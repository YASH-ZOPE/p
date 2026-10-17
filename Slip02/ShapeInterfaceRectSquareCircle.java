import java.util.Scanner;

interface Shape {
    void area();
}

class Rectangle implements Shape {
    double l, b;
    Rectangle(double l, double b) {
        this.l = l;
        this.b = b;
    }
    public void area() {
        System.out.println("Area of Rectangle = " + (l * b));
    }
}

class Square extends Rectangle {
    Square(double s) {
        super(s, s);
    }
    public void area() {
        System.out.println("Area of Square = " + (l * b));
    }
}

class Circle implements Shape {
    double r;
    Circle(double r) {
        this.r = r;
    }
    public void area() {
        System.out.println("Area of Circle = " + (3.14 * r * r));
    }
}

class Demo {
    public static void main(String args[]) {

        Rectangle r = new Rectangle(10,20);
        Square s = new Square(11);
        Circle c = new Circle(8);
        r.area();
        s.area();
        c.area();
    }
}
