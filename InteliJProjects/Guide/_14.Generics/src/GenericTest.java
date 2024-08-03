import java.util.ArrayList;
import java.util.List;

public class GenericTest {
    public static void main(String[] args) {
        List<String> name = new ArrayList<>();
        List<Integer> age = new ArrayList<>();
        List<Number> number = new ArrayList<>();

        name.add("Wang Xishengshun");
        age.add(21);
        number.add(27);

        getData(name);
        getData(age);
        getData(number);

        System.out.println("\n");

        // getUperNumber(name); //报错，因为 String 不是 Number 的子类型
        getUperNumber(age);
        getUperNumber(number);

    }

    public static void getData(List<?> data) {
        System.out.println("data: " + data.get(0));
    }

    public static void getUperNumber(List<? extends Number> data) {
        System.out.println("data: " + data.get(0));
    }
}
