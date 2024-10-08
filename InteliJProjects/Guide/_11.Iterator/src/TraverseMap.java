import java.util.*;

public class TraverseMap {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<String, String>();
        map.put("1", "value1");
        map.put("2", "value2");
        map.put("3", "value3");

        // 第一种，普遍使用，二次取值
        System.out.println("通过Map.keySet遍历key和value：");
        for (String key : map.keySet()) {
            System.out.println("key= " + key + "and value= " + map.get(key));
        }

        // 第二种
        System.out.println("通过Map.entrySet使用iterator遍历key和value：");
        Iterator<Map.Entry<String, String>> ite = map.entrySet().iterator();
        while (ite.hasNext()) {
            Map.Entry<String, String> entry = ite.next();
            System.out.println("key= " + entry.getKey() + "value= " + entry.getValue());
        }

        // 第三种：推荐，尤其是容量大时
        System.out. println("通过Map.entrySet遍历key和value：");
        for (Map.Entry<String, String> entry : map.entrySet()) {
            System.out.println("key= " + entry.getKey() + "value= " + entry.getValue());
        }
    }
}
