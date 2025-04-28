#include "Solution.h"

bool Solution::isSubsequence(string s, string t) {
	int tLen = t.length();
	int sLen = s.length();
	int sPos, tPos;
	sPos = tPos = 0;

	if (sLen == 0)
		return true;

	for (; tPos < tLen; tPos++) {
		if (s[sPos] == t[tPos]) {
			sPos += 1;
		}

		if (sPos == sLen)
			return true;
	}

	return false;

}