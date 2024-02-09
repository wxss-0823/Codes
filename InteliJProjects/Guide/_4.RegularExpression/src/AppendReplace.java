import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AppendReplace {
    private static String REGEX = "a*b";
    private static String INPUT = "aabfooaabfooabfoobkkk";
    private static String REPLACE = "-";

    public static void main(String[] args) {
        Pattern p = Pattern.compile(REGEX);
        Matcher m = p.matcher(INPUT);
        StringBuffer sb = new StringBuffer();

        // 开始匹配
        while (m.find()){
            m.appendReplacement(sb, REPLACE);
        }
        // 当最后一次匹配结束后，后续字符串无法匹配，也无法被替换
        m.appendTail(sb);
        System.out.println(sb);
    }
}
