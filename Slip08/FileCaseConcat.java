import java.io.*;

public class FileCaseConcat {
    public static void main(String[] args) throws Exception {
        // F1 -> F2 : copy contents of F1 into F2 with case changed
        FileReader fr = new FileReader("F1.txt");
        FileWriter fw = new FileWriter("F2.txt");
        int c;
        while ((c = fr.read()) != -1) {
            char ch = (char) c;
            if (Character.isUpperCase(ch))
                fw.write(Character.toLowerCase(ch));
            else if (Character.isLowerCase(ch))
                fw.write(Character.toUpperCase(ch));
            else
                fw.write(ch);
        }
        fr.close();
        fw.close();

        // F3 = F1 + F2
        FileWriter f3 = new FileWriter("F3.txt");
        for (String name : new String[] { "F1.txt", "F2.txt" }) {
            FileReader r = new FileReader(name);
            while ((c = r.read()) != -1)
                f3.write(c);
            r.close();
        }
        f3.close();

        // display F3
        System.out.println("Contents of F3:");
        BufferedReader br = new BufferedReader(new FileReader("F3.txt"));
        String line;
        while ((line = br.readLine()) != null)
            System.out.println(line);
        br.close();
    }
}
