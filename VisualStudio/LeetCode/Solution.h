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
    // Compress
    vector<char>::iterator insertInt(vector<char>& tar, int src, vector<char>::iterator initPosition, int recursionFlag);


public:
    string mergeAlternately(string word1, string word2);
    string gcdOfStrings(string str1, string str2);
    vector<bool> kidWithCandies(vector<int>& candies, int extraCandies);
    bool canPlaceFlowers(vector<int>& flowerbed, int n);
    string reverseVowels(string str);
    string reverWords(string str);
    vector<int> productExceptSelf(vector<int>& nums);
    bool increasingTriplet(vector<int>& nums);
    vector<char> compress(vector<char>& chars);

};
    

    

