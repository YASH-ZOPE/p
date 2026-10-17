import java.io.*;

class UpperCase {
    public static void main(String[] a) throws Exception {
        FileReader f = new FileReader("a.txt");
        FileWriter w = new FileWriter("b.txt");
        int c;
        while ((c = f.read()) != -1) {
            w.write(Character.toUpperCase((char)c));
        }
        f.close();
        w.close();
        System.out.println("File copied in uppercase.");
    }
}
