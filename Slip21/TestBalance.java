class InsufficientFundException extends Exception {
    InsufficientFundException(String msg) {
        super(msg);
    }
}

class SavingAccount {
    int acno;
    String name;
    double bal;

    SavingAccount(int a, String n, double b) {
        acno = a;
        name = n;
        bal = b;
    }

    void deposit(double amt) {
        bal = bal + amt;
        System.out.println("Amount Deposited: " + amt);
    }

    void withdraw(double amt) throws InsufficientFundException {
        if (bal - amt < 500)
            throw new InsufficientFundException("Insufficient Fund");
        bal = bal - amt;
        System.out.println("Amount Withdrawn: " + amt);
    }

    void viewbalance() {
        System.out.println("Balance: " + bal);
    }
}

public class TestBalance {
    public static void main(String[] args) {
        SavingAccount s = new SavingAccount(101, "Rahul", 2000);
        try {
            s.viewbalance();
            s.deposit(500);
            s.withdraw(1800);
            s.viewbalance();
        }
        catch (InsufficientFundException e) {
            System.out.println(e.getMessage());
        }
    }
}
