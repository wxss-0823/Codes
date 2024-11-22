<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CompleteFormExample</title>
</head>
<style>
    .error {color: #FF0000;}
</style>
<body>
    <?php
        // 定义变量并设置为空
        $nameErr = $emailErr = $genderErr = $websiteErr = "";
        $name  = $email = $gender = $comment = $website = "";

        if ($_SERVER['REQUEST_METHOD'] == "POST") {
            if (empty($_POST["name"])) {
                $nameErr = "The name is necessary.";
            } else {
                $name = test_input($_POST["name"]);
                // check name
                if (!preg_match("/^[a-zA-Z ]*$/", $name)) {
                    $nameErr = "Only allow grapheme & space";
                }
            }

            if (empty($_POST["email"])) {
                $emailErr = "The E-mail is necessary.";
            } else {
                $email = test_input($_POST["email"]);
                if (!preg_match("/([\w\-]+@[\w\-]+.[\w\-+])/", $email)) {
                    $emailErr = "Inlegal E-mail address.";
                }
            }

            if (empty($_POST["website"])) {
                $website = "";
            } else {
                $website = test_input($_POST["$website"]);
                if (!preg_match("/b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]/i", $website)) {
                    $websiteErr = "Inlegal URL address.";
                }
            }

            if (empty($_POST["comment"])) {
                $comment = "";
            } else {
                $comment = test_input($_POST["comment"]);
            }

            if (empty($_POST["gender"])) {
                $genderErr = "The gender is necessary.";
            } else {
                $gender = test_input($_POST["gender"]);
            }
        }
        

        function test_input($text) {
            $text = trim($text);
            $text = stripslashes($text);
            $text = htmlspecialchars($text);
            return $text;
        }
    ?>
    <h2> PHP Form confirm</h2>
    <p class="error">* must be input.</p>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST">
        Name: <input type="text" name="name" value="<?php echo $name; ?>">
        <span class="error">* <?php echo $nameErr?></span>
        <br><br>
        E-mail: <input type="text" name="email" value="<?php echo $email; ?>">
        <span class="error">* <?php echo $emailErr; ?></span>
        <br><br>
        Website: <input type="text" name="website" value="<?php echo $website; ?>">
        <span class="error"><?php echo $websiteErr;?></span>
        <br><br>
        PS: <br><textarea name="comment" rows="5" cols="40"><?php echo $comment;?></textarea>
        <br><br>
        Gender: <input type="radio" name="gender" <?php if (isset($gender) && $gender == "female") echo "checked"; ?> value="female">Female
        <input type="radio" name="gender" <?php if (isset($gender) && $gender == "male") echo "checked"; ?> value="male"> Male
        <span class="error">* <?php echo $genderErr; ?></span>
        <br><br>
        <input type="submit" name="submit" value="Submit">
    </form>
    <?php
    echo "<h2>The content of input:</h2>";
    echo $name;
    echo "<br>";
    echo $email;
    echo "<br>";
    echo $website;
    echo "<br>";
    echo $comment;
    echo "<br>";
    echo $gender;
    ?>
</body>
</html>