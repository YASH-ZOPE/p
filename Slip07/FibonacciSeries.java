package Series;

public class FibonacciSeries {
    public void printSeries(int n) {
        int a = 0, b = 1, c;
        System.out.print("Fibonacci Series: ");
        for (int i = 0; i < n; i++) {
            if (i <= 1) {
                c = i;
            } else {
                c = a + b;
                a = b;
                b = c;
            }
            System.out.print(c + " ");
        }
        System.out.println();
    }
}
