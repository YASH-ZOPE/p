public class ReverseNumberCmdLine {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java ReverseNumberCmdLine <number>");
            return;
        }
        int n = Integer.parseInt(args[0]);
        int num = Math.abs(n), rev = 0;
        while (num > 0) {
            rev = rev * 10 + num % 10;
            num /= 10;
        }
        if (n < 0) rev = -rev;
        System.out.println("Original number: " + n);
        System.out.println("Reversed number: " + rev);
    }
}
