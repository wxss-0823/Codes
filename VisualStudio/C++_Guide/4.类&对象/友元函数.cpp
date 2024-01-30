#include <iostream>

using namespace std;

class Box
{
	double width;
	friend void printWidth(Box box);
public:
	void setWidth(double wid);
};

// 成员函数定义
void Box::setWidth(double wid)
{
	this->width = wid;
}

// 请注意：pirntWidth() 不是任何类的成员函数
void printWidth(Box box)
{
	/* 因为 printWidth() 是 Box 的友元，它可以直接访问该类的任何成员 */
	cout << "Width of box: " << box.width << endl;
}

// 程序的主函数
int FriendFunc()
{
	Box box;
	
	// 使用成员函数设置宽度
	box.setWidth(40.0);

	// 使用友元函数输出宽度
	printWidth(box);

	return 0;
}