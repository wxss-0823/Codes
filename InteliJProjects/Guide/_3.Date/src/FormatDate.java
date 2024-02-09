import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class FormatDate {
    public static void main(String[] args){
        String input =  args.length == 0 ? "2024/1/1" : args[0];
        SimpleDateFormat ft1 = new SimpleDateFormat("yyyy/MM/dd");
        try{
            Date t = ft1.parse(input);
            System.out.printf("The %s is parsed as %s\n", input, t);
        }
        catch (ParseException e){
            System.out.println(e);
            System.out.printf("Can't parse input with %s", ft1);
        }
        Date dNow = new Date();
        SimpleDateFormat ft = new SimpleDateFormat("yyyy/MM/dd hh:mm");
        System.out.printf("Time is %s", ft.format(dNow));
    }
}
