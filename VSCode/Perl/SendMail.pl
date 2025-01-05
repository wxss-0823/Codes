use MIME::Lite;
use Net::SMTP;

# 接收邮箱
$to = '2198993328@qq.com';
$cc = $to;
$user = '2198993328@qq.com';
$pass = "gbvqgjrxgjmndidd";

# 发送者
$from = '2198993328@qq.com';
# 标题
$subject = 'Test Mail 1';
$message = 'This is a message.';

$msg = MIME::Lite->new(
    From => $from,
    To => $to,
    Cc => $cc,
    Subject => $subject,
    Type => 'multipart/mixed'
);

$msg->attach (
    Type => 'TEXT',
    Data => $message
);# 指定附件信息

$msg->send('smtp','smtp.qq.com', Debug => 1, SSL => 1, Port => 465, AuthUser=>$user, AuthPass=>$pass);

# print "Main is sent successfully!"