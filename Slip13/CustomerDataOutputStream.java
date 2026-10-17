import java.io.*;
import java.util.*;

class Customer {
    public static void main(String[] a) throws Exception {
        Scanner s = new Scanner(System.in);
        DataOutputStream d = new DataOutputStream(
            new FileOutputStream("customer.txt"));

        System.out.print("Enter number of customers: ");
        int n = s.nextInt();
        s.nextLine();

        for (int i = 0; i < n; i++) {
            System.out.println("\nCustomer " + (i + 1));

            System.out.print("Enter ID: ");
            int id = s.nextInt();
            s.nextLine();

            System.out.print("Enter Name: ");
            String nm = s.nextLine();

            System.out.print("Enter Address: ");
            String ad = s.nextLine();

            System.out.print("Enter Mobile No: ");
            String mb = s.nextLine();

            d.writeBytes("ID: " + id + "\n");
            d.writeBytes("Name: " + nm + "\n");
            d.writeBytes("Address: " + ad + "\n");
            d.writeBytes("Mobile: " + mb + "\n");
            d.writeBytes("------------------\n");
        }
        d.close();
        System.out.println("\nCustomer details stored in customer.txt");
    }
}
