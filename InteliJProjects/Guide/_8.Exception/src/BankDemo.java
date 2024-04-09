import java.io.*;

public class BankDemo {
    public static void main(String[] args) {
        CheckingAccount c = new CheckingAccount(823);
        System.out.println("Depositing $500...");
        c.deposit(500.00);
        try {
            System.out.println("Withdraw $100...");
            c.withdraw(100);
            System.out.println("Withdraw $600...");
            c.withdraw(600);
        } catch (InsufficientFundsException e) {
            System.out.println("Sorry, but you are short " + e.getAmount());
            e.printStackTrace();
        }
    }
}
