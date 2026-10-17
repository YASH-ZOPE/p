import java.util.Scanner;

class CricketPlayer {
    String name;
    int innings, notOut, totalRuns;
    double batAvg;

    CricketPlayer(String name, int innings, int notOut, int totalRuns) {
        this.name = name;
        this.innings = innings;
        this.notOut = notOut;
        this.totalRuns = totalRuns;
    }

    // static method to calculate batting average
    static void avg(CricketPlayer p) {
        try {
            p.batAvg = (double) p.totalRuns / (p.innings - p.notOut);
            if (Double.isInfinite(p.batAvg) || Double.isNaN(p.batAvg))
                throw new ArithmeticException("Innings equal to not-outs");
        } catch (ArithmeticException e) {
            System.out.println("Cannot calculate average for " + p.name + ": " + e.getMessage());
            p.batAvg = 0;
        }
    }

    // static method to sort players on average (ascending)
    static void sortPlayer(CricketPlayer[] p) {
        for (int i = 0; i < p.length - 1; i++)
            for (int j = 0; j < p.length - 1 - i; j++)
                if (p[j].batAvg > p[j + 1].batAvg) {
                    CricketPlayer t = p[j];
                    p[j] = p[j + 1];
                    p[j + 1] = t;
                }
    }

    void display() {
        System.out.println(name + "\t" + innings + "\t" + notOut + "\t" + totalRuns + "\t" + String.format("%.2f", batAvg));
    }
}

public class CricketPlayerSort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of players: ");
        int n = sc.nextInt();
        CricketPlayer[] p = new CricketPlayer[n];
        for (int i = 0; i < n; i++) {
            System.out.print("Enter name, innings, not-outs, total runs of player " + (i + 1) + ": ");
            p[i] = new CricketPlayer(sc.next(), sc.nextInt(), sc.nextInt(), sc.nextInt());
            CricketPlayer.avg(p[i]);
        }
        CricketPlayer.sortPlayer(p);
        System.out.println("\nPlayers sorted by batting average:");
        System.out.println("Name\tInn\tNO\tRuns\tAvg");
        for (CricketPlayer x : p) x.display();
    }
}
