#include <iostream>

using namespace std;

class Box
{
public:
	// 构造函数定义
	Box(double l = 2.0, double b = 2.0, double h = 2.0)
	{
		cout << "调用构造函数" << endl;
		length = l;
		breadth = b;
		height = h;
	}
	double Volume()
	{
		return length * breadth * height;
	}
	bool compare(Box box)
	{
		return this->Volume() > box.Volume();
	}

private:
	double length;	// 长度
	double breadth;	// 宽度
	double height;	// 高度
};

int ThisPtr()
{
	Box Box1(3.3, 1.2, 1.5);	// 声明 box1
	Box Box2(8.5, 6.0, 2.0);	// 声明 box2

	// cout << (bool)Box1.compare(Box2) << endl;

	if (Box1.compare(Box2))
	{
		cout << "Box2 的体积比 Box1 小" << endl;
	}
	else
	{
		cout << "Box2 的体积大于或等于 Box1" << endl;
	}
	return 0;
}