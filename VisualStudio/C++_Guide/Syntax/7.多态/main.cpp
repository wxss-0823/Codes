#include <iostream>

using namespace std;

class Shape
{
protected:
	int width, height;
public:
	// 声明基类构造函数
	Shape(int a = 0, int b = 0)
	{
		width = a;
		height = b;
	}
	// 声明纯虚函数，= 0
	virtual int area() = 0;
};

class Rectangle :public Shape
{
public:
	// 声明继承构造函数
	Rectangle(int a, int b) :Shape(a, b) {}
	// 覆写 area 函数
	int area()
	{
		cout << "Rectangle class area: " << width * height << endl;
		return width * height;
	}
};

class Triangle :public Shape
{
public:
	// 声明继承构造函数
	Triangle(int a, int b) :Shape(a, b) {}
	// 覆写 area 函数
	int area()
	{
		cout << "Triangle class area: " << width * height / 2 << endl;
		return width * height / 2;
	}
};

int main()
{
	Shape* shape;
	Rectangle Rect(3, 4);
	Triangle Tri(4, 7);

	// 存储矩形对象地址
	shape = &Rect;
	// 调用矩形对象的 area 函数
	shape->area();

	// 存储三角形对象地址
	shape = &Tri;
	// 调用三角形对象的 area 函数
	shape->area();

	return 0;
}





