interface Operation {
    double PI = 3.142;
    double area();
    double volume();
}

class Circle implements Operation {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double area() {
        return PI * radius * radius;
    }

    public double volume() {
        return 0;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }
}

class Cylinder implements Operation {
    private double radius;
    private double height;

    public Cylinder(double radius, double height) {
        this.radius = radius;
        this.height = height;
    }

    public double area() {
        return 2 * PI * radius * (radius + height);
    }

    public double volume() {
        return PI * radius * radius * height;
    }
}

class Main {
    public static void main(String[] args) {
        Circle c1 = new Circle(5);
        Cylinder c2 = new Cylinder(5, 10);

        System.out.println("Circle:");
        System.out.println("Area: " +c1.area());
        System.out.println("Volume: " +c1.volume());

        System.out.println("\nCylinder:");
        System.out.println("Surface Area: " +c2.area());
        System.out.println("Volume: " +c2.volume());
    }
}
