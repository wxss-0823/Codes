import com.sun.xml.internal.ws.server.sei.SEIInvokerTube;

import java.util.ArrayList;
import java.util.Iterator;

public class IteratorTest {
    public static void main(String[] args) {
        ArrayList<String> sites = new ArrayList<>();
        sites.add("Google");
        sites.add("WXSS");
        sites.add("TaoBao");
        sites.add("ZhiHu");

        // 获取迭代器
        Iterator<String> it = sites.iterator();

        // 删除元素
        do {
            String i = it.next();
            if (i.length() < 5) {
                it.remove();
            }
        } while(it.hasNext());

        // 重置迭代器
        it = sites.iterator();
        do {
            System.out.println(it.next());
        } while (it.hasNext());
    }
}
