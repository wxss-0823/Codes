#include <iostream>
#include <csignal>
#include <windows.h>

using namespace std;

void signalHandler(int signum)
{
	cout << "Interrupt signal (" << signum << ") received.\n";

	exit(signum);
}

int main()
{
	int i = 0;
	// 注册信号 SIGINT 和信号处理函数
	// 头文件中定义 SIGINT 为2
	signal(SIGINT, signalHandler);

	while (++i)
	{
		cout << "Going to sleep..." << endl;
		if (i == 3)
		{
			raise(SIGINT);
		}
		Sleep(1000);
	}
	return 0;
}