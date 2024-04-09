import java.io.*;

public class CheckingAccount {
    // balance 为余额，number 为卡号
    private double balance;
    private int number;
    public CheckingAccount(int number) {
        this.number = number;
    }
    // 方法：存钱
    public void deposit(double amount) {
        this.balance += amount;
    }
    // 方法：取钱
    public void withdraw(double amount) throws InsufficientFundsException {
        if (amount <= this.balance) {
            this.balance -=amount;
        } else {
            double needs = amount - balance;
            throw new InsufficientFundsException(needs);
        }
    }
    // 方法：返回余额
    public double getBalance() {
        return this.balance;
    }
    // 方法：返回卡号
    public int getNumber() {
        return this.number;
    }
}
