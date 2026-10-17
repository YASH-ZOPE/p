import java.applet.Applet;
import java.awt.Graphics;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

public class MouseEventApplet extends Applet implements MouseListener {
    String msg = "Perform a mouse action";

    public void init() {
        addMouseListener(this);
    }

    public void mouseClicked(MouseEvent e) {
        msg = "Mouse Clicked";
        repaint();
    }

    public void mousePressed(MouseEvent e) {
        msg = "Mouse Pressed";
        repaint();
    }

    public void mouseReleased(MouseEvent e) {
        msg = "Mouse Released";
        repaint();
    }

    public void mouseEntered(MouseEvent e) {
        msg = "Mouse Entered";
        repaint();
    }

    public void mouseExited(MouseEvent e) {
        msg = "Mouse Exited";
        repaint();
    }

    public void paint(Graphics g) {
        g.drawString(msg, 50, 50);
    }
}
