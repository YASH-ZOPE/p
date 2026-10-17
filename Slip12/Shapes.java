import java.applet.Applet;
import java.awt.Graphics;

public class Shapes extends Applet
{
    public void paint(Graphics g)
    {
        g.drawRect(100, 80, 200, 100);
        g.drawOval(100, 220, 200, 100);
    }
}
