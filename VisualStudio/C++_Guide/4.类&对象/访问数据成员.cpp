#include <iostream>

using namespace std;

class Box
{
public :
	double length;	// ����
	double breadth;	// ���
	double height;	// �߶�
	// ��Ա��������
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
	Box Box1;	// ���� Box1������Ϊ Box
	Box Box2;	// ���� Box2������Ϊ Box
	Box Box3;	// ���� Box3������Ϊ Box
	double volume = 0.0;	// ���ڴ洢���

	// Box1 ����
	Box1.length = 5.0;
	Box1.breadth = 6.0;
	Box1.height = 7.0;

	// Box2 ����
	Box2.length = 10.0;
	Box2.breadth = 12.0;
	Box2.height = 13.0;

	// Box3 ����
	Box3.set(16.0, 8.0, 12.0);

	// Box1 �����
	volume = Box1.get();
	cout << "Box1 �������" << volume << endl;

	// Box2 �����
	volume = Box2.get();
	cout << "Box2 �������" << volume << endl;

	// Box3 �����
	volume = Box3.get();
	cout << "Box2 �������" << volume << endl;

	return 0;
}
