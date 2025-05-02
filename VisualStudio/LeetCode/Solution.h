#pragma once
#include <string>
#include <vector>
using namespace std;

class Solution
{
// vector & string
private:
    // GCDOfStrings
    bool isSubStr(string subString, string str);
    string cpyStringNTimes(string str, int times);
    int gcd(int n1, int n2);
    // KidWithCandies
    int findVectorMaxElement(vector<int>& vec);
    // Compress
    vector<char>::iterator insertInt(vector<char>& tar, int src, vector<char>::iterator initPosition, int recursionFlag);

// two-ways pointer
private:
    // MaxOperations
    bool removeTwoAddend(vector<int>& posA, vector<int>& posB, vector<int>& nums, bool parityFlag = 0);

// vector & string
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

// two-way pointer
public:
    vector<int>& moveZeroes(vector<int>& nums);
    bool isSubsequence(string s, string t);
    int maxArea(vector<int>& height);
    int maxOperations(vector<int>& nums, int k);

};
    

    

