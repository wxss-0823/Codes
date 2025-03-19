#include "Resolution.h"
using namespace std;

string Resolution::mergeAlternately(string word1, string word2)
{
    int nFlagLength1, nLength1, nFlagLength2, nLength2, nMaxLength;
    nFlagLength1 = nLength1 = word1.length();
    nFlagLength2 = nLength2 = word2.length();
    nMaxLength = max(nFlagLength1, nFlagLength2);
    string sResult = word1 + word2;

    for (int i = 0; i < nMaxLength; i++)
    {
        nFlagLength1 -= 1;
        nFlagLength2 -= 1;
        if (nFlagLength1 >= 0 && nFlagLength2 >= 0)
        {
            sResult[i * 2] = word1[i];
            sResult[i * 2 + 1] = word2[i];
        }
        else if (nFlagLength1 < 0)
            sResult[nLength1 + i] = word2[i];
        else
            sResult[nLength2 + i + 1] = word1[i];
    }
    return sResult;
}

bool Resolution::isSubStr(string subStr, string str)
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

string Resolution::CpyStringNTimes(string str, int times)
{
    for (int i = 1; i < times; i++)
    {
        str += str;
    }
    return str;
}

string Resolution::gcdOfStrings(string str1, string str2)
{
    int nTempLength = 0;
    int nMatchLength = 1;
    int nStartIndex = 0;
    int nStr1Length = str1.length();
    int nStr2Length = str2.length();
    int nMaxStrLength = max(nStr1Length, nStr2Length);
    string sMinStr, result;

    if (nMaxStrLength == nStr1Length)
    {
        sMinStr = str2;
    }
    else
        sMinStr = str1;

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
            nTempLength = i - nMatchLength;
            nStartIndex += 1;
        }
        else if (nStartIndex != 0)
        {
            nStartIndex = 0;
            i -= 1;
            nMatchLength += nTempLength + 1;
            nTempLength = 0;
        }
        else
        {
            nStartIndex = 0;
            nMatchLength += nTempLength + 1;
            nTempLength = 0;
        }
    }

    string sMinSubStr = sMinStr.substr(0, nMatchLength);
    string sCheckedSubStr = "";
    result = sMinSubStr;

    // find max sub string
    for (int i = 1; i < 10000; i++)
    {
        if ((sMinSubStr.length() * i) <= sMinStr.length())
        {
            sCheckedSubStr = CpyStringNTimes(sMinSubStr, i);
            if (isSubStr(sCheckedSubStr, str1) && isSubStr(sCheckedSubStr, str2))
                result = sCheckedSubStr;
        }
        else
            return result;
    }
}