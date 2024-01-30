#include <iostream>
#include <thread>
#include <Windows.h>

using namespace std;

// һ�����⺯��
void foo(int Z)
{
	for (int i = 0; i < Z; i++)
	{
		cout << "�߳�ʹ�ú���ָ����Ϊ�ɵ��ò���" << endl;
		//Sleep(1000);
	}
}

// �ɵ��ö���
// ������ () �����������������࣬���� + () ����ִ�к���
// ����������������
class thread_obj
{
public:
	thread_obj()
	{
		cout << "���캯������\n" << endl;
	}
	void operator() (int x)
	{
		for (int i = 0; i < x; i++)
		{
			cout << "�߳�ʹ�ú���������Ϊ�ɵ��ò���" << endl;
			//Sleep(1000);
		}
	}
};

int main()
{
	cout << "�߳� 1��2��3 "
		"��������" << endl;
	
	// ����ָ��
	thread th1(foo, 3);

	// ��������
	// ����� () �����أ���ʱ��������ù��캯�������Ǳ�ʾ��������
	thread th2(thread_obj(), 3);

	// ���� lambda ���ʽ
	auto f = [](int x)
		{
			for (int i = 0; i < x; i++)
			{
				cout << "�߳�ʹ�� lamda ���ʽ��Ϊ�ɵ��ò���" << endl;
				//Sleep(1000);
			}
		};

	// �߳�ͨ��ʹ�� lambda ���ʽ��Ϊ�ɵ��ò���
	thread th3(f, 3);

	// �ȴ��߳����
	// �ȴ��߳� t1 ���
	th1.join();

	// �ȴ��߳� t2 ���
	th2.join();

	// �ȴ��߳� t3 ���
	th3.join();

	return 0;
}

