import java.util.Scanner;

class Book {
    int bookId;
    String bookName;
    double price;

    Book(int bookId, String bookName, double price) {
        this.bookId = bookId;
        this.bookName = bookName;
        this.price = price;
    }

    void display() {
        System.out.println("Book Id: " + bookId + "  Name: " + bookName + "  Price: " + price);
    }
}

public class BookArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Book[] b = new Book[5];
        for (int i = 0; i < 5; i++) {
            System.out.println("\nEnter details of book " + (i + 1));
            System.out.print("Book Id: ");   int id = sc.nextInt();
            System.out.print("Book Name: "); String nm = sc.next();
            System.out.print("Price: ");     double p = sc.nextDouble();
            b[i] = new Book(id, nm, p);
        }
        System.out.println("\n--- Book Details ---");
        for (Book x : b) x.display();
    }
}
