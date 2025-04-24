#include "Solution.h";

string Solution::reverWords(string str) {
	char space = ' ';
	int wordHead = 0;
	int wordLength = 0;
	string result = "";
	vector<string> wordList = {};

	// Match space
	for (int i = 0; i < str.length(); i++) {
		if (str[i] == space) {
			wordHead += 1;
		}
		// find word
		else {
			wordLength += 1;
			// check end
			if (wordHead + wordLength == str.length())
				wordList.push_back(str.substr(wordHead, wordLength));

			// compare next char
			if (str[wordHead + wordLength] == space) {
				wordList.push_back(str.substr(wordHead, wordLength));
				wordHead += wordLength;
				wordLength = 0;
			}
		}
	}
	while (!wordList.empty()) {
		result += wordList.size() != 1 ? (wordList.back() + ' ') : wordList.back();
		wordList.pop_back();
	}
	
	return result;
}