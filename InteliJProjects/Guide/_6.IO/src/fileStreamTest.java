import java.io.*;

public class fileStreamTest {
/*
    由于输入是二进制字节，所以存储存在乱码，
    只会读取末八位，高位被丢弃，读取数值也不正确！！！
*/
    public static void main(String[] args) {
        try {
            byte[] bWrite = {1};
            OutputStream os = new FileOutputStream("./_6.IO/test.txt");
            for  (int x = 0; x < bWrite.length; x++) {
                os.write(bWrite[x]); // writes the bytes
            }
            os.close();

            InputStream is = new FileInputStream("test.txt");
            int size = is.available();

            for (int i = 0; i < size; i++) {
                System.out.print(is.read() + ' ');
            }
            is.close();
        } catch (Exception e) {
            System.out.print("Exception: " + e);
        }

    }
}
