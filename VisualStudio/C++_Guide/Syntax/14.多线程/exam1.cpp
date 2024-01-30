#include <iostream>
#include <thread>
#include <Windows.h>

using namespace std;

// 一个虚拟函数
void foo(int Z)
{
	for (int i = 0; i < Z; i++)
	{
		cout << "线程使用函数指针作为可调用参数" << endl;
		//Sleep(1000);
	}
}

// 可调用对象
// 重载了 () 运算符的类叫做函数类，类名 + () 可以执行函数
// 其对象叫做函数对象
class thread_obj
{
public:
	thread_obj()
	{
		cout << "构造函数调用\n" << endl;
	}
	void operator() (int x)
	{
		for (int i = 0; i < x; i++)
		{
			cout << "线程使用函数对象作为可调用参数" << endl;
			//Sleep(1000);
		}
	}
};

int main()
{
	cout << "线程 1、2、3 "
		"独立运行" << endl;
	
	// 函数指针
	thread th1(foo, 3);

	// 函数对象
	// 运算符 () 被重载，此时不代表调用构造函数，而是表示函数对象
	thread th2(thread_obj(), 3);

	// 定义 lambda 表达式
	auto f = [](int x)
		{
			for (int i = 0; i < x; i++)
			{
				cout << "线程使用 lamda 表达式作为可调用参数" << endl;
				//Sleep(1000);
			}
		};

	// 线程通过使用 lambda 表达式作为可调用参数
	thread th3(f, 3);

	// 等待线程完成
	// 等待线程 t1 完成
	th1.join();

	// 等待线程 t2 完成
	th2.join();

	// 等待线程 t3 完成
	th3.join();

	return 0;
}

