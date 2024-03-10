import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BRReadLines {
    public static void main(String[] args) throws IOException {
        String getString;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        do {
            getString = br.readLine();
            System.out.println(getString);
        }while(!getString.equals("end"));
    }
}
