package game;

public class Indoor {
    String game, player;

    public Indoor() {
        game = "Chess";
        player = "2";
    }

    public Indoor(String g, String p) {
        game = g;
        player = p;
    }

    public void display() {
        System.out.println("Indoor Game : " + game);
        System.out.println("Players : " + player);
    }
}
