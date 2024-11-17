<!DOCTYPE html>
<html>
<body>

<?php
echo "Hello World!";
?><br>

<?php
$conn = new mysqli("localhost", "root", "020823");
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
}
echo "连接成功";
?><br>

<?php
    $x = 1;
    $y = 2;
    function test() {
        // 使用 global 关键字使用全局变量
        global $x,$y;
        echo $x + $y;

        // 使用 GLOBALS 数组访问全局变量
        echo $GLOBALS['y'] + $GLOBALS['x'];
    }

    test();
?><br>

<?php
    function add() {
        static $z = 1;
        echo $z ;
        $z++ ;
    }
    add();
    add();
    add();
    add();
?>
</body>