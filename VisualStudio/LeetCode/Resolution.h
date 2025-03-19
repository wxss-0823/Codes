#pragma once
#include <string>
using namespace std;

class Resolution
{
private:
    bool isSubStr(string subString, string str);
    string CpyStringNTimes(string str, int times);

public:
    string mergeAlternately(string word1, string word2);
    string gcdOfStrings(string str1, string str2);
};
    

    

