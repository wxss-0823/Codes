#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	char data[100];
	
	// ��дģʽ���ļ�
	ofstream outfile;
	outfile.open("after.dat");

	cout << "Write to the file." << endl;
	cout << "Enter your name: " << endl;
	cin.getline(data, 100);

	// ���ļ�д���û����������
	outfile << data << endl;

	cout << "Enter your age: " << endl;
	cin >> data;
	cin.ignore();

	// �ٴ����ļ�д���û����������
	outfile << data << endl;

	// �رմ򿪵��ļ�
	outfile.close();

	// �Զ�ģʽ���ļ�
	ifstream infile;
	infile.open("after.dat");

	cout << "Reading from the file." << endl;
	infile >> data;

	// ����Ļ��д������
	cout << data << endl;

	// �ٴδ���Ļ��д�����ݣ�����ʾ��
	infile >> data;
	cout << data << endl;

	// �رմ򿪵��ļ�
	infile.close();

	return 0;

}