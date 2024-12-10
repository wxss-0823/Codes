import redis.clients.jedis.Jedis;

import java.util.Iterator;
import java.util.Set;


public class RedisKeyJava {
    public RedisKeyJava() {
        // 连接本地的 Redis 服务
        try (Jedis jedis = new Jedis("127.0.0.1", 6379)) {
            // 如果 Redis 服务设置了密码，需要下面授权
            jedis.auth("root");
            System.out.println("Connection Successfully!");

            // 获取数据并输出
            Set <String> keys = jedis.keys("*");
            Iterator <String> it = keys.iterator();
            while(it.hasNext()) {
                String key = it.next();
                System.out.println("key: " + key);
            }
        }
    }
}
