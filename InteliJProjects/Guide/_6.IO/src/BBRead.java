import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 使用 BufferedReader 在控制台读取字符
public class BBRead {
    public static void main(String[] args) throws IOException {
        char c;
        // 使用 System.in 创建 BufferedReader 对象
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        do{
            // 调用 read() 函数会抛出异常
            c = (char)br.read();
            System.out.println(c);
        }while(c != 'q');
    }
}
