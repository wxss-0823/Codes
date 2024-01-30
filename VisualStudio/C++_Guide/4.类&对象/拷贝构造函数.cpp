#include <iostream>

using namespace std;

class Line
{
public :
	int getLength(void);
	Line(int len);	// 构造函数
	Line(const Line& obj);	// 拷贝构造函数
	~Line();	// 析构函数

private :
	int* ptr;
};

Line::Line(int len)
{
	cout << "调用构造函数" << endl;
	// 为指针分配内存
	ptr = new int;
	*ptr = len;
}

Line::Line(const Line& obj)
{
	cout << "调用拷贝构造函数为指针 ptr 分配内存" << endl;
	ptr = new int;
	*ptr = *obj.ptr;	// 拷贝值
}

Line::~Line()
{
	cout << "释放内存" << endl;
	delete ptr;
}

int Line::getLength(void)
{
	return *ptr;
}

void display(Line obj)
{
	cout << "line 大小：" << obj.getLength() << endl;
}

int CopyConstructor()
{
	Line line1(10);	// 实例化类时不会调用拷贝构造函数

	Line line2 = line1;	// 对象的赋值时，调用了拷贝构造函数

	display(line1);	// 对象为参数时，调用
	display(line2);

	return 0;
}