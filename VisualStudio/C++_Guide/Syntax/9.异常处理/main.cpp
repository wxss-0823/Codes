#include <iostream>

using namespace std;

struct MyException :public exception
{
	/* ����ֵΪָ���ַ���ָ�룬ֵΪ������
	   ��������Ϊ const����ʾ���޸Ľṹ���Ա����
	   throw() ��ʾ�ڵ��� what() �����ڼ䲻�����쳣
	*/ 
	const char* what() const throw()
	{
		return "C++ Exception.";
	}
};

int main()
{
	try
	{
		// �����ṹ�壬() ���ڳ�ʼ���ṹ�������Ҫ����
		throw MyException();
	}
	catch (MyException& e)
	{
		cout << "MyException caught." << endl;
		cout << e.what() << endl;
	}

	return 0;
}