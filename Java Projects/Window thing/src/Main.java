import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;




public class Main extends JFrame{
    final private Font mainFont = new Font("Segoe print", Font.BOLD, 18);
    JTextField tfFirstName, tfLastName;


    public void initialize(){
        JLabel label = new JLabel("Color change", SwingConstants.CENTER);
        label.setFont(mainFont);

        JButton GreenButton = new JButton("Green");
        GreenButton.setFont(mainFont);
        JButton BlueButton = new JButton("Blue");
        BlueButton.setFont(mainFont);
        JButton RedButton = new JButton("Red");
        RedButton.setFont(mainFont);
        JButton YellowButton = new JButton("Yellow");
        YellowButton.setFont(mainFont);

        JPanel mainPanel = new JPanel(new BorderLayout());
        mainPanel.setBackground(Color.WHITE);

        ActionListener buttonListener = new ActionListener() {
            public void actionPerformed(ActionEvent e){
                String command = e.getActionCommand();
                switch (command){
                    case "Green":
                        mainPanel.setBackground(Color.GREEN);
                        break;
                    case "Blue":
                        mainPanel.setBackground(Color.BLUE);
                        break;
                    case "Red":
                        mainPanel.setBackground(Color.RED);
                        break;
                    case "Yellow":
                        mainPanel.setBackground(Color.YELLOW);
                        break;
                }

            }
        };

        GreenButton.addActionListener(buttonListener);
        BlueButton.addActionListener(buttonListener);
        RedButton.addActionListener(buttonListener);
        YellowButton.addActionListener(buttonListener);

        JPanel bottomPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        bottomPanel.add(BlueButton);
        bottomPanel.add(RedButton);
        bottomPanel.add(GreenButton);
        bottomPanel.add(YellowButton);

        mainPanel.add(label, BorderLayout.CENTER); 
        mainPanel.add(bottomPanel, BorderLayout.SOUTH);

        setTitle("Welcome"); 
        setSize(500, 600);   
        setMinimumSize(new Dimension(300, 400));
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        add(mainPanel);
        setVisible(true);
    }
    public Main() { 
        initialize(); 
    }


    public static void main(String[] args){
        Main myFrame = new Main();
        System.out.print(myFrame);
        
    }
}
