function myFunction() {
    var x, text;

    // 获取 id="numb"的值
    x = document.getElementById("numb").value;

    // 逻辑判定
    if (isNaN(x) || x < 1 || x > 10) {
        text = "输入错误";
    } else {
        text = "输入正确";
    }
    document.getElementById("demo").innerHTML = text;
}