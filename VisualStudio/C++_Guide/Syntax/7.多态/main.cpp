#include <iostream>

using namespace std;

class Shape
{
protected:
	int width, height;
public:
	// �������๹�캯��
	Shape(int a = 0, int b = 0)
	{
		width = a;
		height = b;
	}
	// �������麯����= 0
	virtual int area() = 0;
};

class Rectangle :public Shape
{
public:
	// �����̳й��캯��
	Rectangle(int a, int b) :Shape(a, b) {}
	// ��д area ����
	int area()
	{
		cout << "Rectangle class area: " << width * height << endl;
		return width * height;
	}
};

class Triangle :public Shape
{
public:
	// �����̳й��캯��
	Triangle(int a, int b) :Shape(a, b) {}
	// ��д area ����
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

	// �洢���ζ����ַ
	shape = &Rect;
	// ���þ��ζ���� area ����
	shape->area();

	// �洢�����ζ����ַ
	shape = &Tri;
	// ���������ζ���� area ����
	shape->area();

	return 0;
}





