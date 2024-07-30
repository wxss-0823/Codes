import java.util.ArrayList;
import java.util.Collections;

public class BasicOperations {
    public static void main(String[] args) {
        ArrayList<String> strSites = new ArrayList<String>();
        // 添加元素
        System.out.println("添加元素");
        strSites.add("Google");
        strSites.add("WXSS");
        strSites.add("HUST");
        strSites.add("Education");
        System.out.println(strSites);
        // 访问元素
        System.out.println("访问元素");
        System.out.println(strSites.get(1));    // 访问第二个元素
        // 修改元素
        System.out.println("修改元素");
        strSites.set(2, "Wiki");
        System.out.println(strSites);    // 修改第三个元素
        // 删除元素
        System.out.println("删除元素");
        strSites.remove(3);
        System.out.println(strSites);    // 删除第四个元素
        // 计算大小
        System.out.println("计算大小");
        System.out.println(strSites.size());
        // 迭代列表
        System.out.println("迭代列表");
        for (String str : strSites) {
            System.out.println(str);
        }
        // 存储数字
        System.out.println("存储数字");
        ArrayList<Integer> numSites = new ArrayList<Integer>();
        numSites.add(11);
        numSites.add(22);
        numSites.add(33);
        numSites.add(44);
        System.out.println(numSites);
        // 排序
        System.out.println("排序");
        Collections.sort(strSites);
        Collections.sort(numSites);
        System.out.println(strSites);
        System.out.println(numSites);
    }
}
