function loadXMLWithParserDetect(xmlpath) {
    try { // Internet Explorer
        xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
        xmlDoc.async = false;
        xmlDoc.load(xmlpath);

        if (xmlDoc.parseError.errorCode != 0) {
            alert("Error in line " + xmlDoc.parseError.line + 
                " position " + xmlDoc.parseError.linePos + 
                "nError Code: " + xmlDoc.parseError.errorCode + 
                "nError Reason: " + xmlDoc.parseError.reason + 
                "Error Line: " + xmlDoc.parseError.srcText
            );
            return (null);
        }
    } catch (e) {
        try { // Firefox 
            xmlDoc = document.implementation.createDocument("", "", null);
            xmlDoc.async = false;
            xmlDoc.load(xmlpath);
            if (xmlDoc.documentElement.nodeName == "parsererror") {
                alert(xmlDoc.documentElement.childNodes[0].nodeValue);
                return (null);
            }
        } catch (e) {
            alert(e.message)
        }
    }
    try {
        return (xmlDoc);
    } catch (e) {
        alert(e.message);
    }
    return (null);
}