// 引入 HashMap 包
import java.util.HashMap;

public class HashMapTest {
    public static void main(String[] args) {
        // 定义 整形：字符串映射
        HashMap<Integer, String> Sites1 = new HashMap<>();
        Sites1.put(1, "Google");
        Sites1.put(2, "WXSS");
        Sites1.put(3, "TaoBao");
        Sites1.put(4, "ZhiHu");
        System.out.println(Sites1);

        // 定义 字符串：字符串映射
        HashMap<String, String> Sites2 = new HashMap<>();
        Sites2.put("one", "Google");
        Sites2.put("two", "WXSS");
        Sites2.put("three", "TaoBao");
        Sites2.put("four", "ZhiHu");
        System.out.println(Sites2);

        // 获取值
        System.out.println(Sites2.get("one"));

        // 删除键值对
        Sites1.remove(2);
        System.out.println(Sites1);

        // 计算映射大小
        System.out.println(Sites2.size());

        // for-each 遍历
        for (String i : Sites2.keySet()) {
            System.out.println(i + ": " + Sites2.get(i));
        }
        // 获取键值
        System.out.println(Sites1.keySet());
        // 获取值
        System.out.println(Sites1.values());
    }
}
