import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Counter {
    private static final String REGEX = "\\bcat\\b";
    private static final String INPUT = "cat cat cat cat cat";

    public static void main(String[] args) {
        Pattern re = Pattern.compile(REGEX);
        Matcher m = re.matcher(INPUT);
        int count = 0;

        // 开始逐一寻找匹配项目
        while(m.find()){
            count++;
            System.out.println("Match number: " + count);
            System.out.println("Start at: " + m.start());
            System.out.println("End at: " + m.end());
        }
    }
}
