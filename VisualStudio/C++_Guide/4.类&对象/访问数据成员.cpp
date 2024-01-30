#include <iostream>

using namespace std;

class Box
{
public :
	double length;	// 长度
	double breadth;	// 宽度
	double height;	// 高度
	// 成员函数声明
	double get(void);
	void set(double len, double bre, double hei);
};

double Box::get(void)
{
	return length * breadth * height;
}

void Box::set(double len, double bre, double hei)
{
	length = len;
	breadth = bre;
	height = hei;
}

int AccessToMem()
{
	Box Box1;	// 声明 Box1，类型为 Box
	Box Box2;	// 声明 Box2，类型为 Box
	Box Box3;	// 声明 Box3，类型为 Box
	double volume = 0.0;	// 用于存储体积

	// Box1 详述
	Box1.length = 5.0;
	Box1.breadth = 6.0;
	Box1.height = 7.0;

	// Box2 详述
	Box2.length = 10.0;
	Box2.breadth = 12.0;
	Box2.height = 13.0;

	// Box3 详述
	Box3.set(16.0, 8.0, 12.0);

	// Box1 的体积
	volume = Box1.get();
	cout << "Box1 的体积：" << volume << endl;

	// Box2 的体积
	volume = Box2.get();
	cout << "Box2 的体积：" << volume << endl;

	// Box3 的体积
	volume = Box3.get();
	cout << "Box2 的体积：" << volume << endl;

	return 0;
}
