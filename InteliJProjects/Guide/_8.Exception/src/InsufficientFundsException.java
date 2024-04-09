import java.io.*;

// 自定义异常类，继承自 Exception 类
public class InsufficientFundsException extends Exception
{
    // 此处的 amount 用来存储当出现异常（取出钱多余余额时）所缺乏的钱
    private double amount;
    public InsufficientFundsException(double amount) {
        this.amount = amount;
    }
    public double getAmount() {
        return this.amount;
    }
}
