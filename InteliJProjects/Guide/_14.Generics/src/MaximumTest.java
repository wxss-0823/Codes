public class MaximumTest {
    // 比较三个值并返回最大值
    public static <T extends Comparable<T>> T maxNum(T x, T y, T z) {
        // 假设 x 最大
        T max = x;
        if(y.compareTo(max) > 0) {
            max = y;    // 现在是 y 最大
        }
        if (z.compareTo(max) > 0) {
            max = z;    // 现在是 z 最大
        }
        return max;
    }

    public static void main(String[] args) {
        System.out.printf("%d, %d, %d 中最大的是：%d\n\n",
                2, 3, 1, maxNum(2, 3, 1));

        System.out.printf("%1f, %1f, %1f 中最大的是：%1f\n\n",
                1.2, 4.3, 3.2, maxNum(1.2, 4.3, 3.2));

        System.out.printf("%s, %s, %s 中最大的是：%s\n\n",
                "apple", "orange", "pear", maxNum("apple", "orange", "pear"));
    }
}
