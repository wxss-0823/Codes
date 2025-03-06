<!DOCTYPE html>
<script runat="server">

    Protected Sub Page_Load(sender As Object, e As EventArgs)

    End Sub
</script>

<% 
    Response.Cookies("Wxss")("firstname") = "Xss"
    Response.Cookies("Wxss")("lastname") = "Wang"
    Response.Cookies("Wxss")("country") = "CHN"
    Response.Cookies("Wxss")("age") = 23
%>
<html lang="en">
<body>
<% Response.Write("Hello World!") %>
<form method="get" action="simpleform.asp">
    First Name: <input type="text" name="fname" /><br>
    Last Name: <input type="type" name="lname" /><br>
<input type="submit" value="Submit">
</form>

<!--
    Dim x, y
    For Each x In Request.Cookies
        Response.Write("<p>")
        If Request.Cookies(x).HasKeys Then
            For Each y In Request.Cookies(x)
                Response.Write(x & ":" & y & "=" & Request.Cookies(x)(y))
                Response.Write("<br>")
            Next
        Else
            Response.Write(x & "=" & Request.Cookies(x) & "<br>")
        End If
        Response.Write("</p>")
    Next
-->

<p><!--#include file="header.inc" --></p>
</body>
</html>



