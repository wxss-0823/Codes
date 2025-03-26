#pragma once
#include <string>
#include <vector>
using namespace std;

class Solution
{
private:
    // GCDOfStrings
    bool isSubStr(string subString, string str);
    string cpyStringNTimes(string str, int times);
    int gcd(int n1, int n2);
    // KidWithCandies
    int findVectorMaxElement(vector<int>& vec);


public:
    string mergeAlternately(string word1, string word2);
    string gcdOfStrings(string str1, string str2);
    vector<bool> kidWithCandies(vector<int>& candies, int extraCandies);

};
    

    

