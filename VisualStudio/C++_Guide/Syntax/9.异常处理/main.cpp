#include <iostream>

using namespace std;

struct MyException :public exception
{
	/* 返回值为指向字符的指针，值为常数；
	   函数类型为 const，表示不修改结构体成员变量
	   throw() 表示在调用 what() 函数期间不丢出异常
	*/ 
	const char* what() const throw()
	{
		return "C++ Exception.";
	}
};

int main()
{
	try
	{
		// 丢出结构体，() 用于初始化结构体而不需要名称
		throw MyException();
	}
	catch (MyException& e)
	{
		cout << "MyException caught." << endl;
		cout << e.what() << endl;
	}

	return 0;
}