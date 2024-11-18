<?php
$name = "this is a variable";
$a = <<<EOF
    <h1>Title</h1>
    <p>Paragraph</p>
    this is a string.$name <br>
    "table:\tx, enter:\nx" <br>
    table without \": \t enter without \": \n
EOF;
echo $a;
?>