#include <iostream>

using namespace std;

extern int FriendFunc();
extern int CopyConstructor();
extern int AccessToMem();
extern int ThisPtr();
extern int PtrToClass();
extern int StaticMem();

int main()
{
	// ������Ԫ����ʵ��
	//FriendFunc();
	
	// ���ÿ������캯��ʵ��
	//CopyConstructor();
	
	// ���÷������ݳ�Աʵ��
	//AccessToMem();

	// ����thisָ��ʵ��
	//ThisPtr();

	// ����ָ�����ָ��ʵ��
	//PtrToClass();

	// ������ľ�̬��Աʵ��
	StaticMem();
	return 0;
}