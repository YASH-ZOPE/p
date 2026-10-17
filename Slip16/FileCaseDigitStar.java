import java.io.*;

public class FileCaseDigitStar {
    public static void main(String[] args) throws Exception {
        FileReader fr = new FileReader("source.txt");
        FileWriter fw = new FileWriter("target.txt");
        int c;
        while ((c = fr.read()) != -1) {
            char ch = (char) c;
            if (Character.isUpperCase(ch))
                fw.write(Character.toLowerCase(ch));
            else if (Character.isLowerCase(ch))
                fw.write(Character.toUpperCase(ch));
            else if (Character.isDigit(ch))
                fw.write('*');
            else
                fw.write(ch);
        }
        fr.close();
        fw.close();
        System.out.println("File copied (source.txt -> target.txt) with case changed and digits replaced by '*'.");
    }
}
