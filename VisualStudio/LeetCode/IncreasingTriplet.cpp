#include "Solution.h"

// Two-way tranversal
//bool Solution::increasingTriplet(vector<int>& nums) {
//	int numsLength = nums.size();
//	vector<int> leftMin(numsLength, 0);
//	vector<int> rightMax(numsLength, 0);
//
//	for (int i = 0; i < numsLength; i++) {
//		if (i == 0)
//			continue;
//		else if (i < 2)
//			leftMin[i] = nums[i - 1];
//		else
//			leftMin[i] = nums[i - 1] < leftMin[i - 1] ? nums[i - 1] : leftMin[i - 1];
//	}
//
//	for (int i = numsLength - 1; i >= 0; i--) {
//		if (i == numsLength - 1)
//			continue;
//		else if (i > numsLength - 3) 
//			rightMax[i] = nums[i + 1];
//		else
//			rightMax[i] = nums[i + 1] > rightMax[i + 1] ? nums[i + 1] : rightMax[i + 1];
//	}
//
//	for (int i = 1; i < numsLength - 1; i++) {
//		if (nums[i] > leftMin[i] && nums[i] < rightMax[i])
//			return true;
//	}
//
//	return false;
//
//}

// Greedy algorithm
bool Solution::increasingTriplet(vector<int>& nums) {
	int numsLength = nums.size();
	int tripletFirst = 0;
	int tripletSecond = INT_MAX;
	for (int i = 0; i < numsLength; i++) {
		if (i == 0)
			tripletFirst = nums[0];
		else {
			if (nums[i] > tripletSecond)
				return true;
			else if (nums[i] > tripletFirst)
				tripletSecond = nums[i];
			else
				tripletFirst = nums[i];
		}
	}

	return false;
}