#include <iostream>

using namespace std;

#define MKSTR(x) #x
#define concat(a, b) a ## b

int Operator()
{
	cout << MKSTR(HELLO C++) << endl;

	int x = 10;
	int y = 20;
	int xy = 40;

	cout << "x = " << x << endl;
	cout << "y = " << y << endl;
	cout << "xy = x##y = " << concat(x, y) << endl;

	cout << "Value of __LINE__ : " << __LINE__ << endl;
	cout << "Value of __FILE__ : " << __FILE__ << endl;
	cout << "Value of __DATE__ : " << __DATE__ << endl;
	cout << "Value of __TIME__ : " << __TIME__ << endl;

	return 0;
}