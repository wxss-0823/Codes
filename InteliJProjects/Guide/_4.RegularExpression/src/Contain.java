import java.util.regex.Pattern;

public class Contain {
    public static void main(String[] args){
        String content = "The author is wxss.";
        String pattern = ".*wxss.*";
        Boolean isExist = Pattern.matches(pattern, content);
        System.out.println("字符串中是否存在 wxss: " + isExist);
    }
}
