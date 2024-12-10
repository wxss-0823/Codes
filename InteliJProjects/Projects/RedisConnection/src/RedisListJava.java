import redis.clients.jedis.Jedis;
import java.util.List;

public class RedisListJava {
    public RedisListJava() {
        // 连接本地的 Redis 服务
        try (Jedis jedis = new Jedis("127.0.0.1", 6379)) {
            // 如果 Redis 服务设置了密码，需要下面授权
            jedis.auth("root");
            System.out.println("Connection Successfully!");
            // 存储数据到列表中
            jedis.lpush("site-list", "Douyin");
            jedis.lpush("site-list", "Google");
            jedis.lpush("site-list", "Taobao");
            // 获取存储的数据并输出
            List <String> list = jedis.lrange("site-list", 0, -1);
            for (String s : list) {
                System.out.println("List element: " + s);
            }
        }
    }
}
