use MIME::Lite;

# 接收邮箱
$to = '2198993328@qq.com';
# 抄送者，多个使用逗号隔开
# $cc = '';

# 发送者
$from = '2198993328@qq.com';
# 标题
$subject = 'Test Mail 1';
$message = 'This is a message.';

$msg = MIME::Lite->new(
    From => $from,
    To => $to,
    # Cc => $cc,
    Subject => $subject,
    Date => $message
);

$msg->send;
print "Main is sent successfully!"