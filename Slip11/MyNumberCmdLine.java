class MyNumber {
    private int n;

    MyNumber() {
        n = 0;
    }

    MyNumber(int n) {
        this.n = n;
    }

    boolean isNegative() {
        return n < 0;
    }

    boolean isPositive() {
        return n > 0;
    }

    boolean isOdd() {
        return n % 2 != 0;
    }

    boolean isEven() {
        return n % 2 == 0;
    }
}

public class MyNumberCmdLine {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java MyNumberCmdLine <number>");
            return;
        }
        MyNumber m = new MyNumber(Integer.parseInt(args[0]));
        System.out.println("Number   : " + args[0]);
        System.out.println("Negative : " + m.isNegative());
        System.out.println("Positive : " + m.isPositive());
        System.out.println("Odd      : " + m.isOdd());
        System.out.println("Even     : " + m.isEven());
    }
}
