import com.mysql.cj.protocol.Resultset;

import java.sql.*;

public class ConnectTest {
    // MySql 9.0.1 版本连接 JDBC 驱动名及数据库 URL
    static final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
    static final String DB_URL = "jdbc:mysql://localhost:3306/WXSS" +
            "?useSSL=false&" +
            "allowPublicKeyRetrieval=true&" +
            "serverTimezone=UTC";

    // 数据库用户名及密码
    static final String USER = "root";
    static final String PASS = "020823";

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try {
            // 注册 JDBC 驱动
            Class.forName(JDBC_DRIVER);

            // 打开连接
            System.out.println("Connecting Database...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Connecting Succeed!");

            // 执行查询
            System.out.println("Instancing Object...");
            stmt = conn.createStatement();
            String sql;
            sql = "SELECT id, name, url FROM websites where id < 4;";
            ResultSet rs = stmt.executeQuery(sql);

            // 展开结果集数据库
            while(rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                String url = rs.getString("url");

                // 输出数据
                System.out.print("ID: " + id);
                System.out.print(", 站点名称: " + name);
                System.out.print(", 站点URL: " + url);
                System.out.print("\n");
            }

            // 完成后关闭
            rs.close();
            stmt.close();
            conn.close();
        } catch(Exception e) {
            throw new RuntimeException(e);
        } finally {
            // 关闭资源
            try {
                if(stmt != null) stmt.close();

            } catch(SQLException se) {
                // 不要使用 throw ，finally 中使用会覆盖 try 中的报错
                // throw new RuntimeException(se);
            }
            try {
                if(conn != null) conn.close();

            } catch(SQLException se) {
                // 不要使用 throw ，finally 中使用会覆盖 try 中的报错
                // throw new RuntimeException(se);
            }
        }
    System.out.println("Goodbye!");
    }
}
