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
	vector<int> nums = { 63, 10, 28, 31, 90, 53, 75, 77, 72, 47, 45, 6, 49, 13, 77, 61, 68, 43, 33, 1, 14, 62, 55, 55, 38, 54, 8, 79, 89, 14, 50, 68, 85, 12, 42, 57, 4, 67, 75, 6, 71, 8, 61, 26, 11, 20, 22, 3, 70, 52, 82, 70, 67, 18, 66, 79, 84, 51, 78, 23, 19, 84, 46, 61, 63, 73, 80, 61, 15, 12, 58, 3, 21, 66, 42, 55, 7, 58, 85, 60, 23, 69, 41, 61, 35, 64, 58, 84, 61, 77, 45, 14, 1, 38, 4, 8, 42, 16, 79, 60, 80, 39, 67, 10, 24, 15, 6, 37, 68, 76, 30, 53, 63, 87, 11, 71, 86, 82, 77, 76, 37, 21, 85, 7, 75, 83, 80, 8, 19, 25, 11, 10, 41, 66, 70, 14, 23, 74, 33, 76, 35, 89, 68, 85, 83, 57, 6, 72, 34, 21, 57, 72, 79, 29, 65, 3, 67, 8, 24, 24, 18, 26, 27, 68, 78, 64, 57, 55, 68, 28, 9, 11, 38, 45, 61, 37, 81, 89, 38, 43, 45, 26, 84, 62, 22, 37, 51, 15, 30, 67, 75, 24, 66, 40, 81, 74, 48, 43, 78, 14, 33, 19, 73, 5, 1, 2, 53, 29, 49, 73, 23, 5 };
	//vector<int> nums = { 2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2 };
	int k = 59;
	//int originLen = nums.size();
	//vector<int> numCounter;

	//for (int i = 0; i < k + 1; i++) {
	//	nums.erase(remove(nums.begin(), nums.end(), i), nums.end());
	//	numCounter.push_back(originLen - nums.size());
	//	originLen = nums.size();
	//}

	//for (int i = 0; i < k + 1; i++) {
	//	cout << i << ' ';
	//}

	//cout << "\n";

	//for (int i = 0; i < 10; i++) {
	//	cout << numCounter[i] << ' ';
	//}
	//for (int i = 10; i < numCounter.size(); i++) {
	//	cout << ' ' << numCounter[i] <<  ' ';
	//}
	//
	//cout << "\n";



	//for (int i = 0; i < ceil(k / 2.0 + 0.1); i++) {
	//	cout << i << ' ';
	//}

	//cout << "\n";

	//int sum = 0;

	//for (int i = 0; i < 10; i++) {
	//	cout << min(numCounter[i], numCounter[k - i]) << ' ';
	//	sum += min(numCounter[i], numCounter[k - i]);
	//}
	//for (int i = 10; i < ceil(k / 2.0 + 0.1); i++) {
	//	cout << ' ' << min(numCounter[i], numCounter[k - i]) << ' ';
	//	sum += min(numCounter[i], numCounter[k - i]);
	//}

	int result = solution.maxOperations(nums, k);

	cout << result;

}