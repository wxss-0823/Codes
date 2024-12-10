import redis.clients.jedis.Jedis;

public class RedisJava {
    public RedisJava() {
        // 连接本地的 Redis 服务
        try (Jedis jedis = new Jedis("127.0.0.1", 6379)) {
            // 如果 Redis 服务设置了密码，需要下面授权
            jedis.auth("root");
            System.out.println("Connection Successfully!");
            // 查看服务是否运行
            System.out.println("Server is running: " + jedis.ping());
        }
    }
}
