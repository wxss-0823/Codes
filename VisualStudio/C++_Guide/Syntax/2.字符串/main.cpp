#include <iostream>
#include <string>
using namespace std;

int main()
{
	string str1 = "runoob";
	string str2 = "google";
	string str3;
	int len;

	// ���� str1 �� str3
	str3 = str1;
	cout << "str3 : " << str3 << endl;

	// ���� str1 �� str2
	str3 = str1 + str2;
	cout << "str3 : " << str3 << endl;

	// ���Ӻ�str3 ���ܳ���
	len = str3.size();
	cout << "str3.size() : " << len << endl;

}