#include <iostream>

using namespace std;

extern int FriendFunc();
extern int CopyConstructor();
extern int AccessToMem();
extern int ThisPtr();
extern int PtrToClass();
extern int StaticMem();

int main()
{
	// 调用友元函数实例
	//FriendFunc();
	
	// 调用拷贝构造函数实例
	//CopyConstructor();
	
	// 调用访问数据成员实例
	//AccessToMem();

	// 调用this指针实例
	//ThisPtr();

	// 调用指向类的指针实例
	//PtrToClass();

	// 调用类的静态成员实例
	StaticMem();
	return 0;
}