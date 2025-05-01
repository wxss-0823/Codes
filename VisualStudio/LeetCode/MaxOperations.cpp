#include "Solution.h"


int Solution::removeTwoAddend(vector<int>& posA, vector<int>& posB, vector<int>& nums, bool parityFlag) {
	int operationCounter = 0;
	if (parityFlag) {
		//addend A is equal to addend B
		while (posA.size() >= 2) {
			nums.erase(nums.begin() + posA[0]);
			nums.erase(nums.begin() + posA[1] - 1);
			posA.erase(posA.begin(), posA.begin() + 2);
			operationCounter++;
		}
		posA.clear();
		posB.clear();
	}
	else {
		// addend A is not equal to addend B
		int minLen = min(posA.size(), posB.size());
		for (int i = 0; i < minLen; i++) {
			nums.erase(nums.begin() + posA[i]);
			nums.erase(nums.begin() + posB[i] - (posA[i] < posB[i] ? 1 : 0));
			operationCounter++;
		}
		posA.clear();
		posB.clear();
	}
	return operationCounter;

}

int Solution::maxOperations(vector<int>& nums, int k) {
	// initialize two addends
	int addA = 0;
	int addB = k - addA;
	vector<int> posA, posB;
	int opeTimes = 0;

	for (; addA < ceil(k / 2.0 + 0.1); addA++) {
		addB = k - addA;
		for (int i = 0; i < nums.size(); i++) {
			if (nums[i] == addA) {
				posA.push_back(i);
			}
			if (nums[i] == addB) {
				posB.push_back(i);
			}
		}
		opeTimes += removeTwoAddend(posA, posB, nums, addA == addB ? 1 : 0);
	}

	return opeTimes;
}