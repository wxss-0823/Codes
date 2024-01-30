#include <iostream>

using namespace std;

extern int ConditionCompile();
extern int Operator();

int main()
{
	// 调用条件编译实例
	ConditionCompile();

	// 调用运算符实例
	Operator();

	return 0;
}