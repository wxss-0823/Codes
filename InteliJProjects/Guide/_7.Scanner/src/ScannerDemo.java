import java.util.Scanner;

public class ScannerDemo {
    public static void main(String[] args) {
        // 从键盘接收数据
        Scanner scan = new Scanner(System.in);

        // next 方式接收字符串
        System.out.println("next方式接收：");
        // 判断是否还有输入
        if (scan.hasNext()) {
//            String str1 = scan.next();
            String str1 = scan.nextLine();
            System.out.println("输入的数据为：" + str1);
        }
        System.out.println("请输入数字：");
        double sum = 0;
        int m = 0;
        while (scan.hasNextDouble()) {
            m++;
            sum += scan.nextDouble();
        }
        System.out.println("输入个数：" + m);
        System.out.println("平均值：" + (sum/m));
        scan.close();
    }
}
