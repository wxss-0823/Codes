import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import net.sourceforge.jdpapi.DataProtector;


public class TestCookies {
    static Connection connection = null;
    static String dbPath = "D:\\Program Files (x86)\\Databases\\";
    static String dbName = dbPath + "Cookies";

    private final DataProtector dataProtector;
    public TestCookies() {
        this.dataProtector = new DataProtector();
    }

    private String decrypt(byte[] data) {
        return dataProtector.unprotect(data);
    }

    public static void main(String[] args) {
        try {
            TestCookies testCookies = new TestCookies();
            Class.forName("org.sqlite.JDBC");
            connection = DriverManager.getConnection("jdbc:sqlite:" + dbName, null, null);

            connection.setAutoCommit(false);
            Statement statement = connection.createStatement();
            statement.setQueryTimeout(3);
            String sql = "select * from Cookies where host_key='.bing.com' and name = 'SRCHD';";

            ResultSet resultSet = statement.executeQuery(sql);
            while(resultSet.next()) {
                String name = resultSet.getString("name");
                String value = resultSet.getString("value");
                InputStream inputStream = resultSet.getBinaryStream("encrypted_value");
                ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
                int ch;
                while ((ch = inputStream.read()) != -1) {
                    byteArrayOutputStream.write(ch);
                }
                byte[] b = byteArrayOutputStream.toByteArray();
                byteArrayOutputStream.close();

                System.out.printf(String.format("name=%s value=%s encrypted_value=%s", name, value, testCookies.decrypt(b)));
            }
            resultSet.close();
            connection.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    static {
        System.load("D:\\Users\\ProjectFiles\\Codes\\InteliJProjects\\Projects\\DecryptSqlite3Value_20241023\\assets\\jdpapi-native-1.0.1.dll");
    }
}
