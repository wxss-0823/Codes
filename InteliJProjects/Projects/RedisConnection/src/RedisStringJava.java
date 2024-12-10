import redis.clients.jedis.Jedis;

public class RedisStringJava {
    public RedisStringJava() {
        // 连接本地的 Redis 服务
        try (Jedis jedis = new Jedis("127.0.0.1", 6379)) {
            // 如果 Redis 服务设置了密码，需要下面授权
            jedis.auth("root");
            System.out.println("Connection Successfully!");
            // 设置 Redis 字符串数据
            jedis.set("githubkey","www.github.com/wxss-0823");
            // 获取存储的数据并输出
            System.out.println("String stored in Redis is: " + jedis.get("githubkey"));
        }
    }
}
