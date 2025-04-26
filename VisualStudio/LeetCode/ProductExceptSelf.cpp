#include "Solution.h"

// Time complexity = O(N) Space coplexity = O(N)
//vector<int> Solution::productExceptSelf(vector<int>& nums) {
//	int length = nums.size();
//
//	vector<int> leftProduct(length, 0), rightProduct(length, 0);
//	leftProduct[0] = 1;
//	rightProduct[length - 1] = 1;
//
//	for (int i = 1; i < nums.size(); i++) {
//		leftProduct[i] = nums[i - 1] * leftProduct[i - 1];
//	}
//
//	for (int i = nums.size() - 2; i >= 0; i--) {
//		rightProduct[i] = nums[i + 1] * rightProduct[i + 1];
//	}
//


//	for (int i = 0; i < nums.size(); i++) {
//		nums[i] = leftProduct[i] * rightProduct[i];
//	}
//
//	return nums;
//}

vector<int> Solution::productExceptSelf(vector<int>& nums) {
	int length = nums.size();
	vector<int> result(length, 0);
	result[0] = 1;

	for (int i = 1; i < length; i++) {
		result[i] = nums[i - 1] * result[i - 1];
	}

	int rightProduct = 1;

	for (int i = length - 1; i >= 0; i--) {
		result[i] *= rightProduct;
		rightProduct *= nums[i];
	}

	return result;
}