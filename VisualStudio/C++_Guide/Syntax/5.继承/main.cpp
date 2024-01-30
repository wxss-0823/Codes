#include <iostream>

using namespace std;

// ���� Shape
class Shape
{
public:
	void setWidth(int w)
	{
		width = w;
	}
	void setHeight(int h)
	{
		height = h;
	}
protected:
	int width;
	int height;
};

// ���� PainCost
class PainCost
{
public:
	int getCost(int area)
	{
		return area * 70;
	}
};

// ������ Rectangle
class Rectangle:public Shape, public PainCost
{
public:
	int getArea()
	{
		return width * height;
	}
};

int main()
{
	Rectangle Rect;
	int area;

	Rect.setWidth(5);
	Rect.setHeight(6);

	area = Rect.getArea();

	// �����������
	cout << "Total area: " << area << endl;
	cout << "Total cost: " << Rect.getCost(area) << endl;

}