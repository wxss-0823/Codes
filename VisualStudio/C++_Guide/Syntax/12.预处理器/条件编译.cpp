#include <iostream>

using namespace std;

#define DEBUG
#define MIN(a, b) (((a) < (b)) ? a : b) 

int ConditionCompile()
{
	int i, j;
	i = 100;
	j = 30;
#ifdef DEBUG
	cout << "Trace: Inside main function." << endl;
#endif // DEBUG

#if 0
	/* 这里是注释，一定不会执行 */
	cout << MKSTR(HELLO C++) << endl;
#endif

	cout << "The minimum is " << MIN(i, j) << endl;

#ifdef DEBUG
	cerr << "Trace: Coming out of main function." << endl;
#endif

	return 0;

}