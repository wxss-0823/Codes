import java.util.*;

public class IteratorExample {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("Hello");
        list.add("World");
        list.add("HAHA HAHA");
        // 第一种方法，使用 For-Each 遍历列表
        for (String str : list) {
            System.out.println(str);
        }

        // 第二种方法，使用 数组 遍历列表
        String[] array = new String[list.size()];
        list.toArray(array);
        for (int i = 0; i < list.size(); i++) {
            System.out.println(array[i]);
        }

        // 第三种方法，使用 迭代器 遍历列表
        Iterator<String> ite = list.iterator();
        while (ite.hasNext()) {
            System.out.println(ite.next());
        }
    }
}
