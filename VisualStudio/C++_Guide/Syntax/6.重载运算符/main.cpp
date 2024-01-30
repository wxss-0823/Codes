#include <iostream>

using namespace std;

class Box
{
public:
	friend Box operator+(const Box& obj1, const Box& obj2);
	double getVolume()
	{
		return length * breadth * height;
	}
	void setLength(double len)
	{
		length = len;
	}
	void setBreadth(double bre)
	{
		breadth = bre;
	}
	void setHeight(double hei)
	{
		height = hei;
	}

private:
	double length;
	double breadth;
	double height;
};

// �ǳ�Ա�����������������Ҫ������������
Box operator+ (const Box& obj1, const Box& obj2)
{
	Box box;
	box.length = obj1.length + obj2.length;
	box.breadth = obj1.breadth + obj2.breadth;
	box.height = obj1.height + obj2.height;
	return box;
}

int main()
{
	Box Box1;
	Box Box2;
	Box Box3;
	double volume = 0.0;

	// Box1 ����
	Box1.setLength(6.0);
	Box1.setBreadth(7.0);
	Box1.setHeight(5.0);

	// Box2 ����
	Box2.setLength(12.0);
	Box2.setBreadth(13.0);
	Box2.setHeight(10.0);

	// Box1 �����
	volume = Box1.getVolume();
	cout << "Volume of Box1: " << volume << endl;

	// Box2 �����
	volume = Box2.getVolume();
	cout << "Volume of Box2: " << volume << endl;

	// ������ӵ�����
	Box3 = Box1 + Box2;

	// Box3 �����
	volume = Box3.getVolume();
	cout << "Volume of Box3: " << volume << endl;

	return 0;
}