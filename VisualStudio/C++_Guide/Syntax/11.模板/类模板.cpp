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
	vector<T> elems;	// 元素
public:
	void push(const T&);	// 入栈函数
	void pop();				// 出栈函数
	T top() const;			// 返回栈顶元素
	bool empty() const		// 元素为空返回 true
	{
		return elems.empty();
	}
};

template <typename T>
void Stack<T>::push(const T& elem)
{
	// 追加传入元素的副本
	elems.push_back(elem);
}

template <typename T>
void Stack<T>::pop()
{
	if (elems.empty())
	{
		throw out_of_range("Stack<>::pop(): empty stack");
	}
	// 删除最后一个元素
	elems.pop_back();
}

template <typename T>
T Stack<T>::top() const
{
	if (elems.empty())
	{
		throw out_of_range("Stack<>::pop(): empty stack");
	}
	// 返回最后一个元素的副本
	return elems.back();
}

int TemplateClass()
{
	try
	{
		Stack<int> intstack;	// 声明整形的类
		Stack<string> stringstack;	// 声明字符串类型的类

		// 操作 int 类型的类
		intstack.push(7);
		cout << intstack.top() << endl;
		intstack.pop();

		// 操作 string 类型的类
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
