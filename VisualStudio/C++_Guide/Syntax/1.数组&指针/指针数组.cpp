#include <iostream>
using namespace std;

void func1();
void func2();

int main()
{
	func2();
	func1();
}

void func1()
{
	/* 定义一个二维数组 */
	int a[3][4] = { {1, 2, 3, 4},
				{5, 6, 7, 8},
				{9, 10, 11, 12} };
	/* 定义数组指针，是一个指向数组的指针 */
	/* 并将二维数组的首地址赋给指针 */
	int(*p)[4] = a;

	/* 指针加 1 指向的是二维数组第二行的首地址 */
	cout << a[1] << endl;
	cout << p++ << endl;

	/* 下一行可以索引 p 指针所指向的当前行的任意元素 */
	cout << (*p)[2] << endl;
	/* 下一行可以索引 p 指针所指向的任意行的第一个元素 */
	cout << *p[0];
}

void func2()
{
	/* 定义一个二维数组*/
	int a[3][4] = { {1, 2, 3, 4},
			{5, 6, 7, 8},
			{9, 10, 11, 12} };

	/* 定义一个指针数组，用于存放指针变量的数组 */
	int* q[3];
	for (int i = 0; i < 3; i++)
	{
		q[i] = a[i];
		cout << q[i] << endl;
		cout << *q[i] << endl;
	}
}