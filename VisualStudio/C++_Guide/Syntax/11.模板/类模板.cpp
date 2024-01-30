#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
#include <stdexcept>

using namespace std;

template <typename T>
class Stack
{
private:
	vector<T> elems;	// Ԫ��
public:
	void push(const T&);	// ��ջ����
	void pop();				// ��ջ����
	T top() const;			// ����ջ��Ԫ��
	bool empty() const		// Ԫ��Ϊ�շ��� true
	{
		return elems.empty();
	}
};

template <typename T>
void Stack<T>::push(const T& elem)
{
	// ׷�Ӵ���Ԫ�صĸ���
	elems.push_back(elem);
}

template <typename T>
void Stack<T>::pop()
{
	if (elems.empty())
	{
		throw out_of_range("Stack<>::pop(): empty stack");
	}
	// ɾ�����һ��Ԫ��
	elems.pop_back();
}

template <typename T>
T Stack<T>::top() const
{
	if (elems.empty())
	{
		throw out_of_range("Stack<>::pop(): empty stack");
	}
	// �������һ��Ԫ�صĸ���
	return elems.back();
}

int TemplateClass()
{
	try
	{
		Stack<int> intstack;	// �������ε���
		Stack<string> stringstack;	// �����ַ������͵���

		// ���� int ���͵���
		intstack.push(7);
		cout << intstack.top() << endl;
		intstack.pop();

		// ���� string ���͵���
		stringstack.push("Wxss");
		cout << stringstack.top() << endl;
		stringstack.pop();
		stringstack.pop();
	}
	catch (const exception& e)
	{
		cerr << "Exception: " << e.what() << endl;
	}

	return 0;
}
