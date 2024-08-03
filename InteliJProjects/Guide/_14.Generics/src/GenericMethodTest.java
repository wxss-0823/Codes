public class GenericMethodTest {
    // 泛型方法 printArray
    public static <E> void printArray(E[] inputArray) {
    /*
        泛型函数需要在返回值类型前，标注泛型类型<...>
        形参为泛型参数
    */
        // 输出数组元素
        for (E element : inputArray) {
            System.out.printf("%s, ", element);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // 创建不同类型的数组
        Integer[] intArray = {1, 2, 3, 4, 5};
        Double[] doubleArray = {1.0, 2.0, 3.0, 4.0, 5.0};
        Character[] charArray = {'H', 'E', 'L', 'L', 'O'};

        System.out.println("整形数组元素为：");
        printArray(intArray);

        System.out.println("\n双精度型数组元素为：");
        printArray(doubleArray);

        System.out.println("\n字符串型数组元素为：");
        printArray(charArray);
    }
}
