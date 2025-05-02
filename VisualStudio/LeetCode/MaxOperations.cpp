#include "Solution.h"
#include <iostream>


bool Solution::removeTwoAddend(vector<int>& posA, vector<int>& posB, vector<int>& nums, bool parityFlag) {
	if (parityFlag) {
		//addend A is equal to addend B
		while (posA.size() >= 2) {
			nums.erase(nums.begin() + posA[0]);
			nums.erase(nums.begin() + posA[1] - 1);
			posA.clear();
			posB.clear();
		}
	}
	else {
		// addend A is not equal to addend B
		int minLen = min(posA.size(), posB.size());
		nums.erase(nums.begin() + posA[0]);
		nums.erase(nums.begin() + posB[0] - (posA[0] < posB[0] ? 1 : 0));
		posA.clear();
		posB.clear();
	}
	return true;

}

int Solution::maxOperations(vector<int>& nums, int k) {
	// initialize two addends
	int addA = 0;
	int addB = k - addA;
	vector<int> posA, posB;
	int opeTimes = 0;

	// dubug var
	vector<int> everyOpe;
	int debugOpeTimes = 0;

	for (; addA < ceil(k / 2.0 + 0.1); addA++) {
		addB = k - addA;
		for (int i = 0; i < nums.size(); i++) {
			if (nums[i] == addA) {
				posA.push_back(i);
			}
			if (nums[i] == addB) {
				posB.push_back(i);
			}
			if (addA != addB) {
				if (posA.size() >= 1 && posB.size() >= 1) {
					removeTwoAddend(posA, posB, nums);
					opeTimes++;
					i = 0;
				}
			}
			else {
				if (posA.size() >= 2 && posB.size() >= 2) {
					removeTwoAddend(posA, posB, nums, 1);
					opeTimes++;
					i = 0;
				}
			}
		}
	}

	//	everyOpe.push_back(min(posA.size(), posB.size()));

	//}
	//for (int index = 0; index < everyOpe.size(); index++) {
	//	debugOpeTimes += everyOpe[index];
	//}

	//for (int i = 0; i < everyOpe.size(); i++) {
	//	cout << i << ' ';
	//}

	//cout << "\n";

	//for (int i = 0; i < 10; i++) {
	//	cout << everyOpe[i] << ' ';
	//}
	//for (int i = 10; i < everyOpe.size(); i++) {
	//cout << ' ' << everyOpe[i] << ' ';
	//}


	return opeTimes;
	
}