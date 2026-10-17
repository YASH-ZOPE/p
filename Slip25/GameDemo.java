import game.*;

class Demo {
    public static void main(String args[]) {
        Indoor i = new Indoor("Table Tennis", "2");
        Outdoor o = new Outdoor("Football", "11");
        i.display();
        o.display();
    }
}
