import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegexExample {
    public static void main(String[] args){
        String line = "This order was placed for QT3000! OK?";
        String pattern = "(\\D*)(\\d+)(.*)";
        Pattern re1 = Pattern.compile(pattern);
        // 返回一个匹配，包含匹配表达式和待匹配行，但未进行匹配
        Matcher m = re1.matcher(line);
        // 进行匹配
        m.find();
        System.out.println(m.group(1));
    }
}
