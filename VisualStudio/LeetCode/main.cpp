#include <iostream>
#include <sstream>
#include "Solution.h"
using namespace std;


int main() {
	Solution solution;

	// call mergeAlternately
	//string result = solution.mergeAlternately("ab", "pqrs");

	// call gcdOfStrings
	//string result = solution.gcdOfStrings("AABBAABBAA", "AABB");

	// call kidWithCandies
	//vector<int> vec = { 2, 3, 5, 1, 3 };
	//vector<bool> result = solution.kidWithCandies(vec, 3);

	// call canPlaceFlowers
	//vector<int> flowerbed = {0, 0, 0, 0, 1};
	//int num = 3;
	//bool result = solution.canPlaceFlowers(flowerbed, num);

	// call reverseVowels
	//string s = "leetcode";
	//string result = solution.reverseVowels(s);

	// call reverseWords
	//string str = "a good   example";
	//string result = solution.reverWords(str);

	// call productExceptSelf
	//vector<int> nums = { 1, 2, 3, 4 };
	//vector<int> result = solution.productExceptSelf(nums);
	//for (int i = 0; i < nums.size(); i++) {
	//	cout << result[i] << ' ';
	//}

	// call increasingTriplet
	//vector<int> nums = { 1 };
	//bool result = solution.increasingTriplet(nums);

	// call compress
	//vector<char> chars = { 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 
	//'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c'};
	//vector<char> result = solution.compress(chars);
	//for (auto i : result) {
	//	cout << i << ' ';
	//}

	// call moveZeroes
	//vector<int> nums = { 0, 1, 0, 3, 12 };
	//vector<int> result = solution.moveZeroes(nums);
	//for (auto e : result) {
	//	cout << e << ' ';
	//}

	// call isSubsequence
	//string s, t;
	//s = "axc", t = "ahbgdc";
	//bool result = solution.isSubsequence(s, t);

	// call maxArea
	//vector<int> height = { 1, 1 };
	//int result = solution.maxArea(height);

	// call maxOperations
	//vector<int> nums = { 73, 74, 74, 71, 68, 67, 45, 1, 24, 2, 26, 48, 82, 82, 28, 60, 19, 36, 26, 9, 12, 83, 1, 86, 18, 78, 14, 66, 20, 26, 4, 80, 44, 35, 53, 48, 74, 25, 75, 47, 31, 20, 59, 10, 35, 24, 26, 3, 48, 69, 78, 43, 12, 86, 37, 49, 1, 90, 20, 35, 58, 20, 2, 20, 16, 18, 88, 25, 44, 63, 12, 16, 64, 41, 86, 87, 2, 23, 14, 63, 43, 60, 47, 7, 23, 11, 64, 53, 71, 78, 82, 56, 65, 25, 27, 52, 89, 68, 63, 14, 48 };
	//int k = 44;
	//int result = solution.maxOperations(nums, k);

	// call findMaxAverage
	vector<int> nums = { 9,7,3,5,6,2,0,8,1,9 };
	int k = 6;
	double result = solution.findMaxAverage(nums, k);

	cout << result;

}