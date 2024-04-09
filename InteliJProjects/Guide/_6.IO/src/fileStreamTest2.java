import java.io.*;

public class fileStreamTest2 {
    public static void main(String[] args) throws IOException{

        // 构建 FileOutPutStream 对象，文件不存在会自动创建
        File f = new File("./_6.IO/test.txt");
        FileOutputStream fop = new FileOutputStream(f);

        // 构建 OutputStreamWriter 对象，参数可以指定编码，默认为操作系统编码，windows 上是 gbk
        OutputStreamWriter writer = new OutputStreamWriter(fop, "UTF-8");

        // 写入到缓存区
        writer.append("中文输入");

        // 换行
        writer.append("\r\n");

        // 刷新缓存区，写入到文件中，如果下面没有要写入的内容，直接 close 也会写入
        writer.append("English");
        writer.append("1234");

        // 关闭写入流，同时会把缓冲区的内容写入文件，所以上面注释掉
        writer.close();

        // 关闭输出流，释放系统资源
        fop.close();

        // 构建 FileInputStream 对象
        FileInputStream fip = new FileInputStream(f);

        // 创建 InputStreamReader 对象，编码与写入相同
        InputStreamReader reader = new InputStreamReader(fip, "UTF-8");

        StringBuffer sb = new StringBuffer();
        while(reader.ready()) {
            // 强制转换为 char 添加到 StringBuffer 中
            sb.append((char) reader.read());
        }
        System.out.println(sb.toString());
        // 关闭读取流
        reader.close();

        // 关闭输入流，释放系统资源
        fip.close();
    }
}
