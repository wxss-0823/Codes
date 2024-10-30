function loadXMLDoc(xmlpath) {
/*
    用于从 xml 文件中加载 DOM 对象
*/
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest;
    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.open("GET", xmlpath, true);
    xmlhttp.send();
    return xmlhttp.responseXML;
}

function loadXMLString(textpath) {
/*
    用于从 text 文件中加载 DOM 对象
*/
    if (window.XMLHttpRequest) {
        parse = new DOMParser();
        xmlDoc = parse.parseFromString(textpath, "text/xml");
    } else {
        xmlDoc = new ActiveXObject("Microsoft.XMLHTTP");
        xmlDoc.async = false;
        xmlDoc.loadXMLDoc(textpath);
    }
    return xmlDoc;
}