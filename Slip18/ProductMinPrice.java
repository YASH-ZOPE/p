import java.util.Scanner;

class Product {
    int id;
    String name;
    double price;

    Product(int id, String name, double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }
}

public class ProductMinPrice {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Product[] p = new Product[5];
        for (int i = 0; i < 5; i++) {
            System.out.print("Enter id, name, price of product " + (i + 1) + ": ");
            p[i] = new Product(sc.nextInt(), sc.next(), sc.nextDouble());
        }
        int min = 0;
        for (int i = 1; i < 5; i++)
            if (p[i].price < p[min].price) min = i;
        System.out.println("\nProduct with minimum price: " + p[min].name + " (Price = " + p[min].price + ")");
    }
}
