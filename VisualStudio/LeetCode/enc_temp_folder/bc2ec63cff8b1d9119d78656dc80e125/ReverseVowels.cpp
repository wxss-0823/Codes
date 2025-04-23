#include "Solution.h"


string Solution::reverseVowels(string s) {
	vector<char> vowelList = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' };
	vector<char> vowelContained = {};
	vector<int>	vowelPos = {};

	// find vowels and their positon
	for (int i = 0; i < s.length() - 1; i++) { 
		for (char vowelLetter : vowelList)
			if (s[i] == vowelLetter)
			{
				vowelContained.insert(vowelContained.end(), s[i]);
				vowelPos.insert(vowelPos.end(), i);
				break;
			}
	}

	// reverse vowels
	for (int i = 0; i < vowelPos.size(); i++) {
		s[vowelPos[i]] = vowelContained[vowelPos.size() - i - 1];
	}

	return s;
}