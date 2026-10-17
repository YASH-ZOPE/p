import java.util.Scanner;

interface Integer {
    void check();
}

class Num implements Integer {
    int n;
    Num(int n) {
        this.n = n;
    }
    public void check() {
        if (n >= 0)
            System.out.println("Positive Number");
        else
            System.out.println("Negative Number");
    }
}

class Demo {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Number: ");
        int n = sc.nextInt();
        Num ob = new Num(n);
        ob.check();
    }
}
