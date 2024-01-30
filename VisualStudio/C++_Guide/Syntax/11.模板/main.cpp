#include <iostream>

using namespace std;

extern int TemplateFunc();
extern int TemplateClass();

int main()
{
	// 执行函数模板实例
	//TemplateFunc();

	// 执行类模板实例
	TemplateClass();

	return 0;
}