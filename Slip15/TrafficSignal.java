import java.applet.Applet;
import java.awt.Graphics;
import java.awt.Color;

public class TrafficSignal extends Applet implements Runnable
{
    Thread t;
    int signal = 1;
    public void init()
    {
        t = new Thread(this);
        t.start();
    }
    public void run()
    {
        while(true)
        {
            signal++;
            if(signal > 3)
                signal = 1;
            repaint();
            try
            {
                Thread.sleep(2000);
            }
            catch(Exception e)
            {
            }
        }
    }
    public void paint(Graphics g)
    {
        g.drawRect(100, 50, 80, 200);
        if(signal == 1)
        {
            g.setColor(Color.RED);
            g.fillOval(120, 70, 40, 40);
        }
        else if(signal == 2)
        {
            g.setColor(Color.YELLOW);
            g.fillOval(120, 130, 40, 40);
        }
        else
        {
            g.setColor(Color.GREEN);
            g.fillOval(120, 190, 40, 40);
        }
    }
}
