import java.util.HashSet;

public class HashSetTest {
    public static void main(String[] args) {
        HashSet<String> sites = new HashSet<String>();
        sites.add("Google");
        sites.add("WXSS");
        sites.add("TaoBao");
        sites.add("ZhiHu");
        System.out.println("添加元素的输出：" + sites);
        // 包含 True
        System.out.println("判断是否包含：" + sites.contains("ZhiHu"));
        // 不包含 False
        System.out.println("       " + sites.contains("Zhihu"));
        // 删除元素 WXSS
        sites.remove("WXSS");
        System.out.println("删除元素的输出：" + sites);
        System.out.println("集合的大小：" + sites.size());
        for (String i : sites) {
            System.out.println(i);
        }
    }
}
