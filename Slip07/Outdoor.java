package game;

public class Outdoor {
    String game, player;

    public Outdoor() {
        game = "Cricket";
        player = "11";
    }

    public Outdoor(String g, String p) {
        game = g;
        player = p;
    }

    public void display() {
        System.out.println("Outdoor Game : " + game);
        System.out.println("Players : " + player);
    }
}
