import javax.swing.*;
public class GermWorld {
    public static void main (String []args) {
        int num1 = Integer.parseInt( JOptionPane.showInputDialog("Enter number 1"));
        int num2 = Integer.parseInt(JOptionPane.showInputDialog("Enter number 2"));
        int product = num1 - num2;
        JOptionPane.showMessageDialog(null,product); 
    }
}