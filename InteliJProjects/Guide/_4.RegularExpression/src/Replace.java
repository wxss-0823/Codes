import java.time.temporal.TemporalField;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Replace {
    private static String REGEX = "dog";
    private static String INPUT = "The dog says meow. " +
            "All dogs say meow.";
    private static String REPLACE = "cat";

    public static void main(String[] args) {
        Pattern pattern = Pattern.compile(REGEX);
        Matcher m = pattern.matcher(INPUT);
        // 替换第一个匹配
        INPUT = m.replaceFirst(REPLACE);
        System.out.println(INPUT);
        // 替换全部匹配
        INPUT = m.replaceAll(REPLACE);
        System.out.println(INPUT);
    }
}
