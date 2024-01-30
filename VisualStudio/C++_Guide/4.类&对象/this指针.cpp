#include <iostream>

using namespace std;

class Box
{
public:
	// ���캯������
	Box(double l = 2.0, double b = 2.0, double h = 2.0)
	{
		cout << "���ù��캯��" << endl;
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
	double length;	// ����
	double breadth;	// ���
	double height;	// �߶�
};

int ThisPtr()
{
	Box Box1(3.3, 1.2, 1.5);	// ���� box1
	Box Box2(8.5, 6.0, 2.0);	// ���� box2

	// cout << (bool)Box1.compare(Box2) << endl;

	if (Box1.compare(Box2))
	{
		cout << "Box2 ������� Box1 С" << endl;
	}
	else
	{
		cout << "Box2 ��������ڻ���� Box1" << endl;
	}
	return 0;
}