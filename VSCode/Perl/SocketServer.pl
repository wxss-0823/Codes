use strict;
use Socket;

# 使用端口 7890 作为默认值
my $port = shift || 7890;
my $proto = getprotobyname('tcp');
my $server = "localhost";

# 创建 socket，端口可重复使用，创建多个连接
socket(SOCKET, PF_INET, SOCK_STREAM, $proto)
    or die "Can't open socket $!\n";
setsockopt(SOCKET, SOL_SOCKET, SO_REUSEADDR, 1)
    or die "Can't set SO_REUSEADDR $!\n";

# 绑定端口并监听
bind(SOCKET, pack_sockaddr_in($port, inet_aton($server)))
    or die "Can't bind port $! \n";

listen(SOCKET, 5) or die "listen: $! \n";
print "Access is running: $port \n";

# 接收请求
my $client_addr;
while ($client_addr = accept(NEW_SCOKET, SOCKET)) {
    # 发送消息并关闭连接
    my $name = gethostbyaddr($client_addr, AF_INET);
    print NEW_SCOKET "A message come from server.";
    print "Connection recieved from $name\n";
    close NEW_SCOKET;
}
