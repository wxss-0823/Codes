#include <iostream>

using namespace std;

class Box
{
	double width;
	friend void printWidth(Box box);
public:
	void setWidth(double wid);
};

// ��Ա��������
void Box::setWidth(double wid)
{
	this->width = wid;
}

// ��ע�⣺pirntWidth() �����κ���ĳ�Ա����
void printWidth(Box box)
{
	/* ��Ϊ printWidth() �� Box ����Ԫ��������ֱ�ӷ��ʸ�����κγ�Ա */
	cout << "Width of box: " << box.width << endl;
}

// �����������
int FriendFunc()
{
	Box box;
	
	// ʹ�ó�Ա�������ÿ��
	box.setWidth(40.0);

	// ʹ����Ԫ����������
	printWidth(box);

	return 0;
}