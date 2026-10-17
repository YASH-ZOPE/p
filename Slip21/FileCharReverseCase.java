import java.io.*;

public class FileCharReverseCase {
    public static void main(String[] args) throws Exception {
        FileReader fr = new FileReader("input.txt");
        int c;
        while ((c = fr.read()) != -1) {
            char ch = (char) c;
            if (Character.isUpperCase(ch))
                System.out.println(ch + " -> " + Character.toLowerCase(ch));
            else if (Character.isLowerCase(ch))
                System.out.println(ch + " -> " + Character.toUpperCase(ch));
            else if (Character.isDigit(ch))
                System.out.println(ch + " -> Digit");
            else if (ch == ' ')
                System.out.println("' ' -> Space");
        }
        fr.close();
    }
}
