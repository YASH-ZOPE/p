import java.util.Scanner;

class Customer {
    int cid;
    String cname;
    double billAmount;

    Customer(int cid, String cname, double billAmount) {
        this.cid = cid;
        this.cname = cname;
        this.billAmount = billAmount;
    }
}

public class CustomerSort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of customers: ");
        int n = sc.nextInt();
        Customer[] c = new Customer[n];
        for (int i = 0; i < n; i++) {
            System.out.print("Enter cid, cname, billAmount of customer " + (i + 1) + ": ");
            c[i] = new Customer(sc.nextInt(), sc.next(), sc.nextDouble());
        }
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - 1 - i; j++)
                if (c[j].billAmount > c[j + 1].billAmount) {
                    Customer t = c[j];
                    c[j] = c[j + 1];
                    c[j + 1] = t;
                }
        System.out.println("\nCustomers sorted by bill amount (ascending):");
        for (Customer x : c)
            System.out.println("ID: " + x.cid + "  Name: " + x.cname + "  Bill: " + x.billAmount);
    }
}
