import java.io.*;

public class PrimesBufferedReader {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter a number: ");
        int n = Integer.parseInt(br.readLine());
        System.out.println("Prime numbers up to " + n + ":");
        for (int i = 2; i <= n; i++) {
            boolean prime = true;
            for (int j = 2; j <= i / 2; j++)
                if (i % j == 0) {
                    prime = false;
                    break;
                }
            if (prime)
                System.out.print(i + " ");
        }
        System.out.println();
    }
}
