use strict;
use Socket;

# 初始化地址与端口
my $host = shift || "localhost";
my $port = shift || 7890;
my $proto = getprotobyname('tcp');
my $server = "localhost";

# 创建 socket，端口可重复使用，创建多个连接
socket(SOCKET, PF_INET, SOCK_STREAM, ($proto)[2])
    or die "Can't open socket $!\n";
connect(SOCKET, pack_sockaddr_in($port, inet_aton($server)))
    or die "Can't connect: port $port! \n";

my $line;
while($line = <SOCKET>) {
    print "$line \n";
}

close SOCKET or die "close: $!";