import java.io.*;
import java.util.*;

public class FileReverse {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter file name (e.g. input.txt): ");
        String name = sc.next();

        BufferedReader br = new BufferedReader(new FileReader(name));
        StringBuilder sb = new StringBuilder();
        int c;
        while ((c = br.read()) != -1) sb.append((char) c);
        br.close();

        System.out.println("Contents in reverse order:");
        System.out.println(sb.reverse());
    }
}
