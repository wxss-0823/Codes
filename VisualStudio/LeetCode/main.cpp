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
	vector<int> flowerbed = {0, 0, 0, 0, 1};
	int num = 3;
	bool result = solution.canPlaceFlowers(flowerbed, num);

	cout << result;

}