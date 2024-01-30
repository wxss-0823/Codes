#include <iostream>

using namespace std;

class Line
{
public :
	int getLength(void);
	Line(int len);	// ���캯��
	Line(const Line& obj);	// �������캯��
	~Line();	// ��������

private :
	int* ptr;
};

Line::Line(int len)
{
	cout << "���ù��캯��" << endl;
	// Ϊָ������ڴ�
	ptr = new int;
	*ptr = len;
}

Line::Line(const Line& obj)
{
	cout << "���ÿ������캯��Ϊָ�� ptr �����ڴ�" << endl;
	ptr = new int;
	*ptr = *obj.ptr;	// ����ֵ
}

Line::~Line()
{
	cout << "�ͷ��ڴ�" << endl;
	delete ptr;
}

int Line::getLength(void)
{
	return *ptr;
}

void display(Line obj)
{
	cout << "line ��С��" << obj.getLength() << endl;
}

int CopyConstructor()
{
	Line line1(10);	// ʵ������ʱ������ÿ������캯��

	Line line2 = line1;	// ����ĸ�ֵʱ�������˿������캯��

	display(line1);	// ����Ϊ����ʱ������
	display(line2);

	return 0;
}