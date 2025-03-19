#include <iostream>
#include "Resolution.h"
using namespace std;


int main() {
	Resolution resolution;

	// call mergeAlternately
	//string result = resolution.mergeAlternately("ab", "pqrs");
	//cout << result;

	// call gcdOfStrings
	string result = resolution.gcdOfStrings("OBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNO", "OBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNO");
	cout << result;

}