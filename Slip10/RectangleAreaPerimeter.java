import java.util.Scanner;

class Rectangle {
    double length, breadth;

    Rectangle(double length, double breadth) {
        this.length = length;
        this.breadth = breadth;
    }

    double area() {
        return length * breadth;
    }

    double perimeter() {
        return 2 * (length + breadth);
    }
}

public class RectangleAreaPerimeter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter length and breadth: ");
        Rectangle r = new Rectangle(sc.nextDouble(), sc.nextDouble());
        System.out.println("Area      = " + r.area());
        System.out.println("Perimeter = " + r.perimeter());
    }
}
