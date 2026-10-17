import java.io.*;

class TextRead {
    public static void main(String[] a) throws Exception {
        FileReader f = new FileReader("a.txt");
        BufferedReader b = new BufferedReader(f);
        int c = 0, l = 0, w = 0;
        String s;
        while ((s = b.readLine()) != null) {
            l++;
            c += s.length();
            String[] x = s.trim().split("\\s+");
            if (!s.trim().isEmpty())
                w += x.length;
        }
        b.close();
        System.out.println("Characters = " + c);
        System.out.println("Lines = " + l);
        System.out.println("Words = " + w);
    }
}
