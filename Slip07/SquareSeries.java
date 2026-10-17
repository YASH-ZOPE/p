package Series;

public class SquareSeries {
    public void printSeries(int n) {
        System.out.print("Squares of Numbers: ");
        for (int i = 1; i <= n; i++) {
            System.out.print((i * i) + " ");
        }
        System.out.println();
    }
}
