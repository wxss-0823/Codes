use MIME::Lite;

# 接收邮箱
$to = 'wangxishengshun@gmail.com';
$user = '2198993328@qq.com';
$pass = "gbvqgjrxgjmndidd";

# 发送者
$from = '2198993328@qq.com';
# 标题
$subject = 'Test Mail 1';
$message = "This is a message.";

$msg = MIME::Lite->new(
    From => $from,
    To => $to,
    Subject => $subject,
    Data => $message
);

$msg->send('smtp','smtp.qq.com', Debug => 1, SSL => 1, Port => 465, Timeout=>60, AuthUser=>$user, AuthPass=>$pass);
# $msg->send();

print "Main is sent successfully!"