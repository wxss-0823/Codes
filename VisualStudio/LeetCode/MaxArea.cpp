#include "Solution.h"

int Solution::maxArea(vector<int>& height) {
	int hLen = height.size();
	int lIndex, rIndex;
	lIndex = 0, rIndex = hLen - 1;
	int curIndex, curArea;
	int maxArea = 0;
	bool innerExitFlag, outerExitFlag = 0;

	while (!outerExitFlag) {
		curIndex = height[lIndex] < height[rIndex] ? lIndex : rIndex;

		curArea = height[curIndex] * (rIndex - lIndex);

		maxArea = curArea >= maxArea ? curArea : maxArea;
		
		if (curIndex == lIndex) {
			while (!outerExitFlag) {
				if (height[curIndex + 1] >= height[curIndex] || curIndex + 2 >= rIndex) {
					lIndex = curIndex + 1;
					outerExitFlag = 1;
				}
				else
					curIndex++;
			}
		}
		else {
			while (!outerExitFlag) {
				if (height[curIndex - 1] >= height[curIndex] || curIndex - 2 <= lIndex) {
					rIndex = curIndex - 1;
					outerExitFlag = 1;
				}
				else
					curIndex--;
			}
		}

		// restore flag
		outerExitFlag = lIndex == rIndex ? 1 : 0;
	}

	return maxArea;
}