use strict;
use DBI;

my $host = "localhost";         # 主机地址
my $driver = "mysql";           # 接口类型
my $database = "wxss";          # 数据库
# 驱动程序对象的句柄
my $dsn = "DBI:$driver:database=$database:$host";
my $userid = "root";            # 数据库用户名
my $password = "020823";        # 数据库密码

# 连接数据库
my $dbh = DBI->connect($dsn, $userid, $password) or die $DBI::errstr;
my $sth = $dbh->prepaer("SELECT * FROM users;");    # 预处理 SQL 语句
$sth->exeute();                 # 执行 SQL 操作

# 注释这部分使用的是绑定值操作
# $id = 1;
# my $sth = $dbh->prepare("SELECT username FROM users WHERE id > ?")
# $sth->execute($id);

# 循环输出所有数据
while (my @row = $sth->fetchrow_array()) {
    print join('\t', @row) . "\n";
}

$sth->finish();
$dbh->disconnect();
