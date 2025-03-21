#pragma once
#include <string>
using namespace std;

class Resolution
{
private:
    bool isSubStr(string subString, string str);
    string cpyStringNTimes(string str, int times);
    int gcd(int n1, int n2);

public:
    string mergeAlternately(string word1, string word2);
    string gcdOfStrings(string str1, string str2);
};
    

    

