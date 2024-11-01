<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="/">
        <h2>My CD Collection</h2>
        <table border="1">
            <tr bgcolor="#9acd32">
                <th style="text-align:left">Title</th>
                <th style="text-align:left">Artist</th>
            </tr>
        <xsl:for-each select="CATALOG/CD">
            <tr>
                <td bgcolor="#DCE2F1">
                    <xsl:value-of select="TITLE"/>
                </td>
                <td bgcolor="#EAEAEF">
                    <xsl:value-of select="ARTIST"/>
                </td>
            </tr>
        </xsl:for-each>
        </table>
    </xsl:template>
</xsl:stylesheet>