#include <iostream>
#include "Resolution.h"
using namespace std;


int main() {
	Resolution resolution;
	string result = resolution.mergeAlternately("ab", "pqrs");
	cout << result;
}