<!DOCTYPE html>
<html>
<body>

<?php
echo "Hello World!";
?>

<?php
$conn = new mysqli("localhost", "root", "020823");
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
}
echo "连接成功";
?>

</body>