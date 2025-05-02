#include "Solution.h"
#include <iostream>


int Solution::maxOperations(vector<int>& nums, int k) {
	int opeTimes = 0;
	int nLen = nums.size();
	unordered_map<int, int> numMap;

	for (int i = 0; i < nLen; i++) {
		if (nums[i] <= k) {
			numMap[nums[i]]++;
		}
	}

	for (auto e : numMap) {
		if (e.first != k / 2.0)
			opeTimes += min(e.second, numMap[k - e.first]);
		else
			opeTimes += floor(e.second / 2.0) * 2;
	}

	for (auto e : numMap) {
		cout << e.first << ": " << e.second;
		cout << "\n";
	}

	return opeTimes / 2;
}