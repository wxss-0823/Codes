#include "Solution.h";

double Solution::findMaxAverage(vector<int>& nums, int k) {
	int nLen = nums.size();
	double initAvg = 0.0;
	double nextAvg = 0.0;
	double maxAvg = 0.0;

	// initialize
	for (int i = 0; i < k; i++) {
		initAvg += nums[i];
	}
	initAvg /= k;
	maxAvg = initAvg;
	
	if (nLen != k) {
		for (int i = 0; i < nLen - k; i++) {
			nextAvg = initAvg + (nums[i + k] - nums[i] + 0.0) / k;
			maxAvg = nextAvg >= maxAvg ? nextAvg : maxAvg;
			initAvg = nextAvg;
		}
		return maxAvg;
	}
	else
		return initAvg;
}