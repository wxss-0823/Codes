#include <iostream>	

using namespace std;

template <typename T>
/* 通过 T& 来创建变量的引用，函数参数及返回值均是引用类型 */
inline const T& Max(const T& a, const T& b)
{
	return a < b ? b : a;
}

int TemplateFunc()
{
	int i = 39;
	int j = 20;
	cout << "Max(i, j): " << Max<int>(i, j) << endl;

	double f1 = 13.5;
	double f2 = 20.7;
	cout << "Max(f1, f2): " << Max<double>(f1, f2) << endl;

	string s1 = "Hello";
	string s2 = "World";
	// 字符串的比较比较复杂
	cout << "Max(s1, s2): " << Max<string>(s1, s2) << endl;

	return 0;
}
