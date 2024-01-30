#include <iostream>

using namespace std;

class Box_c
{
public:
	static int objectCount;
	// ���캯������
	Box_c(double l = 2.0, double b = 2.0, double h = 2.0)
	{
		cout << "Constructor Called." << endl;
		length = l;
		breadth = b;
		height = h;
		// ÿ�δ�������ʱ���� 1
		objectCount++;
	}
	Box_c(const Box_c& box)
	{
		this->length = box.length;
		this->breadth = box.breadth;
		this->height = box.height;
		// ��������ʱ���� 1
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

// ��ʼ���� Box �ľ�̬��Ա
int Box_c::objectCount = 0;

int StaticMem()
{
	// ��������֮ǰ������������
	cout << "Inital Stage Count: " << Box_c::getCount() << endl;

	Box_c Box1(3.3, 1.2, 1.5);	// ���� box1
	Box_c Box2(8.5, 6.0, 2.0);	// ���� box2

	// �ڴ�������֮��������������
	cout << "Final Stage Count: " << Box_c::getCount() << endl;

	// ��������
	Box_c Box3 = Box2;
	// �����������
	cout << "After Copy: " << Box_c::getCount() << endl;

	return 0;
}