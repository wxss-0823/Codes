import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Match {
    private static final String REGEX = "foo";
    private static final String INPUT1 = "foooooooooooo";
    private static final String INPUT2 = "ooofooooooo";
    private static Pattern pattern;
    private static Matcher matcher1;
    private static Matcher matcher2;

    public static void main(String[] args) {
        pattern = Pattern.compile(REGEX);
        matcher1 = pattern.matcher(INPUT1);
        matcher2 = pattern.matcher(INPUT2);

        System.out.println("Current REGEX is: " + REGEX);
        System.out.println("Current INPUT1 is: " + INPUT1);
        System.out.println("Current INPUT2 is: " + INPUT2);

        // 不要求整句匹配，且从头开始
        System.out.println("lookingAt: " + matcher1.lookingAt());
        // 要求整句匹配
        System.out.println("matches: " + matcher1.matches());
        // 不要求整句匹配，且不从开始
        System.out.println("lookingAt: " + matcher2.lookingAt());
        // 要求整句匹配
        System.out.println("matches: " + matcher2.matches());
    }

}
