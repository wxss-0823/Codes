function showSite(str) {
    if (str == "") {
        document.getElementById("txtHint").innerHTML="";
        return;
    }
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    }
    else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
        {
            document.getElementById("txtHint").innerHTML = xmlhttp.responseText;
        }
    }
    xmlhttp.open("GET", "ajax.php?q="+str, true);
    xmlhttp.send();
}