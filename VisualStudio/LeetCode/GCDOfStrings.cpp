#include "Solution.h"


bool Solution::isSubStr(string subStr, string str)
{
    if (str.length() % subStr.length() != 0)
        return false;
    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] != subStr[i % subStr.length()])
            return false;
    }
    return true;
}

string Solution::cpyStringNTimes(string str, int times)
{
    string cpyString;
    for (int i = 0; i < times; i++)
    {
        cpyString += str;
    }
    return cpyString;
}

int Solution::gcd(int greater, int less)
{
    return less == 0 ? greater : gcd(less, greater % less);
}

string Solution::gcdOfStrings(string str1, string str2)
{
    int nTempLength = 0;
    int nMatchLength = 1;
    int nStartIndex = 0;
    int nStr1Length = str1.length();
    int nStr2Length = str2.length();
    int nMaxStrLength = max(nStr1Length, nStr2Length);
    string sMinStr, sMaxStr, result;

    if (nMaxStrLength == nStr1Length)
    {
        sMinStr = str2;
        sMaxStr = str1;
    }
    else
    {
        sMinStr = str1;
        sMaxStr = str2;
    }

    for (int i = 0; i < nMaxStrLength; i++)
    {
        if (str1[i % nStr1Length] != str2[i % nStr2Length])
            return result = "";
    }

    // find min sub string
    for (int i = 1; i < sMinStr.length(); i++)
    {
        // the next char is equal to the start positon
        if (sMinStr[i] == sMinStr[nStartIndex % nMatchLength])
        {
            nTempLength = i - nMatchLength + 1;
            nStartIndex += 1;
            // nTempLength = nStartIndex == nMatchLength ? 0 : nTempLength;
            // nStartIndex = nStartIndex == nMatchLength ? 0 : nStartIndex;
        }
        else if (nStartIndex != 0)
        {
            nStartIndex = 0;
            i -= nTempLength;
            nMatchLength += 1;
            nTempLength = 0;
        }
        else
        {
            nStartIndex = 0;
            nMatchLength += 1;
            nTempLength = 0;
        }
    }

    string sMinSubStr = sMinStr.substr(0, nMatchLength);
    string sCheckedSubStr = "";
    result = isSubStr(sMinSubStr, str1) && isSubStr(sMinSubStr, str2) ? sMinSubStr : "";

    // find max sub string
    for (int i = 1; i < 10000; i++)
    {
        if (sMinSubStr.length() == 1)
            return cpyStringNTimes(sMinSubStr, gcd(sMaxStr.length(), sMinStr.length()));

        if ((sMinSubStr.length() * i) <= sMinStr.length())
        {
            sCheckedSubStr = cpyStringNTimes(sMinSubStr, i);
            if (isSubStr(sCheckedSubStr, str1) && isSubStr(sCheckedSubStr, str2))
                result = sCheckedSubStr;
        }
        else
            return result;
    }
}