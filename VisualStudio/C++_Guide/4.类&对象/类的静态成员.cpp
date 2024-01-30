#include <iostream>

using namespace std;

class Box_c
{
public:
	static int objectCount;
	// 构造函数定义
	Box_c(double l = 2.0, double b = 2.0, double h = 2.0)
	{
		cout << "Constructor Called." << endl;
		length = l;
		breadth = b;
		height = h;
		// 每次创建对象时增加 1
		objectCount++;
	}
	Box_c(const Box_c& box)
	{
		this->length = box.length;
		this->breadth = box.breadth;
		this->height = box.height;
		// 拷贝对象时增加 1
		objectCount++;
	}
	~Box_c()
	{
		cout << "Destructor Called." << endl;
	}

	double Volume()
	{
		return length * breadth * height;
	}
	static int getCount()
	{
		return objectCount;
	}
private:
	double length;
	double breadth;
	double height;
};

// 初始化类 Box 的静态成员
int Box_c::objectCount = 0;

int StaticMem()
{
	// 创建对象之前输出对象的总数
	cout << "Inital Stage Count: " << Box_c::getCount() << endl;

	Box_c Box1(3.3, 1.2, 1.5);	// 声明 box1
	Box_c Box2(8.5, 6.0, 2.0);	// 声明 box2

	// 在创建对象之后输出对象的总数
	cout << "Final Stage Count: " << Box_c::getCount() << endl;

	// 拷贝对象
	Box_c Box3 = Box2;
	// 输出对象总数
	cout << "After Copy: " << Box_c::getCount() << endl;

	return 0;
}