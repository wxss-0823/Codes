<?php
$q = isset($_GET['q']) ? htmlspecialchars($_GET['q']) : '';
if ($q) {
    if ($q == 'HOME') {
        echo <<<EOF
        <a href="https://github.com/wxss0823/">wxss's homepage<br/></a>
        EOF;
    } else if ($q == 'TUTORIAL') {
        echo <<<EOF
        <a href="https://github.com/wxss0823/">wxss's tutotials<br/></a>
        EOF;
    }
} else {
?>
<form action="" method="get">
    <select name="q">
        <option value="">Please select an option!</option>
        <option value="HOME">Home</option>
        <option value="TUTORIAL">Tutorial</option>
    </select>
    <input type="submit" value="Submit">
</form>
<?php
}
?>

