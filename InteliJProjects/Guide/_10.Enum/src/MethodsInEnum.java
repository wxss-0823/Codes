public class MethodsInEnum {
    public static void main(String[] args) {
        // 调用 values()
        Color[] arr = Color.values();

        // 迭代枚举
        for(Color col : arr) {
            // 查看索引
            System.out.println(col + "at index " + col.ordinal());
        }

        // 使用 valueOf 返回枚举常量
        System.out.println(Color.valueOf("Red"));
    }
}
