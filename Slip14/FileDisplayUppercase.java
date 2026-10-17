import java.io.*;

public class FileDisplayUppercase {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new FileReader("abc.txt"));
        String line;
        System.out.println("Contents of abc.txt in uppercase:");
        while ((line = br.readLine()) != null)
            System.out.println(line.toUpperCase());
        br.close();
    }
}
