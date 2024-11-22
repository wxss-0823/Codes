<p>Welcome</p>
<?php
// 如果 用户输入 <script>location.href = 'http://www.runoob.com';</script>
// 那么 php 文件运行的同时会跳转页面
echo $_POST["fname"];
?><br>
<p>Your age is </p>
<?php
echo $_POST["age"];
?>