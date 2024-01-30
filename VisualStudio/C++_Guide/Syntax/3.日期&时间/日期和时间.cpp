#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <ctime>

using namespace std;

void getNowTime();
void getNowTimeBytm();

int main()
{
	// ��ȡ��ǰʱ���� UTC ʱ��
	getNowTime();
	// ���ýṹ�� tm ��ȡʱ��
	getNowTimeBytm();
}

void getNowTime()
{
	// ���ڵ�ǰϵͳ�ĵ�ǰ����/ʱ��
	time_t now = time(0);

	// �� now ת��Ϊ�ַ�����ʽ
	char* dt = ctime(&now);

	cout << "�������ں�ʱ�䣺" << dt << endl;

	// �� now ת��Ϊ tm �ṹ
	tm* gmtm = gmtime(&now);
	dt = asctime(gmtm);

	cout << "UTC ���ں�ʱ�䣺" << dt << endl;
}

void getNowTimeBytm()
{
	// ���ڵ�ǰϵͳ�ĵ�ǰ����/ʱ��
	time_t now = time(0);

	cout << "1970 ��Ŀǰ����������" << now << endl;

	tm* ltm = localtime(&now);

	// ��� tm �ṹ�ĸ�����ɲ���
	cout << "�꣺" << 1900 + ltm->tm_year << endl;
	cout << "�£�" << 1 + ltm->tm_mon << endl;
	cout << "�գ�" << ltm->tm_mday << endl;
	cout << "ʱ�䣺" << ltm->tm_hour << ":";
	cout << ltm->tm_min << ":";
	cout << ltm->tm_sec << endl;
}