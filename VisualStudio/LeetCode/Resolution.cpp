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