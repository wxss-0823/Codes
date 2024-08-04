import com.sun.mail.util.MailSSLSocketFactory;

import java.security.GeneralSecurityException;
import java.util.*;
import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class SendEmail {
    public static void main(String[] args) {
        // 收件人邮箱
        //String to = "wangxishengshun@gmail.com";
        //String to = "2198993328@qq.com";
        String to = "2890344780@qq.com";

        // 发件人邮箱
        //String from = "2198993328@qq.com";
        String from = "wangxishengshun@gmail.com";

        // 指定发送邮件的主机
        String server = "smtp.gmail.com";

        // 获取系统属性
        Properties properties = System.getProperties();

        // 设置邮件服务器
        properties.setProperty("mail.smtp.host", server);
        properties.put("mail.smtp.auth", "true");
//        properties.setProperty("mail.user", "2198993328@qq.com");
//        properties.setProperty("mail.password", "ufayxgvopwlpdiei");

        // 设置 SSL 加密
        try {
            MailSSLSocketFactory sf = new MailSSLSocketFactory();
            sf.setTrustAllHosts(true);
            properties.put("mail.smtp.ssl.enable", "true");
            properties.put("mail.smtp.ssl.socketFactory", sf);
        } catch(GeneralSecurityException e) {
            throw new RuntimeException(e);
        }

        // 获取默认 session 对象
        Session session = Session.getDefaultInstance(properties, new Authenticator() {
            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication("wangxishengshun@gmail.com", "fcvfcszqydquhjqa");
                //new PasswordAuthentication("2198993328@qq.com", "ufayxgvopwlpdiei");
            }
        });

        try {
            // 创建默认的 MimeMessage 对象
            MimeMessage message = new MimeMessage(session);

            // Set From: 头部头字段
            message.setFrom(new InternetAddress(from));

            // Set To: 头部头字段
            message.setRecipient(Message.RecipientType.TO, new InternetAddress(to));

            // Set Subject: 头部头字段
            message.setSubject("This is the Subject line!");

            // Set Message Body
            message.setText("This is actual message.");

            message.saveChanges();

            // 发送消息
            Transport.send(message);
            System.out.println("Sent message successfully...");
        } catch (javax.mail.MessagingException e) {
            throw new RuntimeException(e);
        }
    }
}
