import Series.FibonacciSeries;
import Series.CubeSeries;
import Series.SquareSeries;
import java.util.Scanner;

public class SeriesMain {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of terms (n): ");
        int n = sc.nextInt();

        FibonacciSeries f = new FibonacciSeries();
        CubeSeries c = new CubeSeries();
        SquareSeries s= new SquareSeries();
        f.printSeries(n);
        c.printSeries(n);
        s.printSeries(n);
    }
}
