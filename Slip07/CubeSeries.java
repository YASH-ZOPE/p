package Series;

public class CubeSeries {
    public void printSeries(int n) {
        System.out.print("Cubes of Numbers: ");
        for (int i = 1; i <= n; i++) {
            System.out.print((i * i * i) + " ");
        }
        System.out.println();
    }
}
