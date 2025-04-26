#include "Solution.h"

vector<char>::iterator Solution::insertInt(vector<char>& tar, int src, vector<char>::iterator initPosition, int recursionFlag = 0) {
	/*
		tar: a char vector to store multi bits integer data

		src: multi bits integer data

		initPosition: the position after the data where the data is inserted in

		recursionFlag: flag the recursion times

		return: the position where after the last insertion data
	*/
	vector<char>::iterator itr;
	if (recursionFlag == 0 && src == 1)
		return initPosition;
	else if (src > 9) {
		itr = tar.insert(initPosition, src % 10 + '0');
		recursionFlag += 1;
		return insertInt(tar, floor(src / 10), itr, recursionFlag);
	}
	else
		return tar.insert(initPosition, src + '0') + recursionFlag + 1;
}

vector<char> Solution::compress(vector<char>& chars) {
	char currentChar = chars[0];
	int repeatCounter = 1;

	// modify the vector
	for (vector<char>::iterator itr = chars.begin() + 1; itr != chars.end(); itr++) {
		if (*itr == currentChar) {
			repeatCounter += 1;
			itr = chars.erase(itr);
			itr -= 1;
		}
		else {
			currentChar = *itr;
			itr = insertInt(chars, repeatCounter, itr);
			repeatCounter = 1;
		}
	}

	insertInt(chars, repeatCounter, chars.end());

	return chars;

}