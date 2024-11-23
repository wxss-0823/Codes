<?php
$allowedExts = array("git","jpeg","jpg","png") ;
$temp = explode(".", $_FILES["file"]["name"]);
echo "File size: " . $_FILES["file"]["size"] . "<br>";
$extention = end($temp);
if ((($_FILES)["file"]["type"] == "image/gif")
|| (($_FILES)["file"]["type"] == "image/jpeg")
|| (($_FILES)["file"]["type"] == "image/jpg")
|| (($_FILES)["file"]["type"] == "image/pjpeg")
|| (($_FILES)["file"]["type"] == "image/x-png")
|| (($_FILES)["file"]["type"] == "image/png")
&& (($_FILES)["file"]["size"] < 204800)
&& in_array($extention, $allowedExts)) 
{
    if ($_FILES["file"]["error"] > 0)
    {
        echo "Error: ". $_FILES["file"]["error"] ."<br>";
    } else {
        echo "File name: " . $_FILES["file"]["name"] . "<br>";
        echo "File type: " . $_FILES["file"]["type"] . "<br>";
        echo "File size: " . $_FILES["file"]["size"] . "<br>";
        echo "File tmp directory: " . $_FILES["file"]["tmp_name"] . "<br>";
    }
    if (file_exists("Upload/" . $_FILES["file"]["name"])) {
        echo $_FILES["file"]["name"] . " File already exist.";
    } else {
        move_uploaded_file($_FILES["file"]["tmp_name"],"Upload/" . $_FILES["file"]["name"]);
        echo "File is docked in " . "Upload/" . $_FILES["file"]["name"];
    }
}
?>