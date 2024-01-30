#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <ctime>

using namespace std;

void getNowTime();
void getNowTimeBytm();

int main()
{
	// 获取当前时间与 UTC 时间
	getNowTime();
	// 利用结构体 tm 获取时间
	getNowTimeBytm();
}

void getNowTime()
{
	// 基于当前系统的当前日期/时间
	time_t now = time(0);

	// 把 now 转化为字符串形式
	char* dt = ctime(&now);

	cout << "本地日期和时间：" << dt << endl;

	// 把 now 转化为 tm 结构
	tm* gmtm = gmtime(&now);
	dt = asctime(gmtm);

	cout << "UTC 日期和时间：" << dt << endl;
}

void getNowTimeBytm()
{
	// 基于当前系统的当前日期/时间
	time_t now = time(0);

	cout << "1970 到目前经过秒数：" << now << endl;

	tm* ltm = localtime(&now);

	// 输出 tm 结构的各个组成部分
	cout << "年：" << 1900 + ltm->tm_year << endl;
	cout << "月：" << 1 + ltm->tm_mon << endl;
	cout << "日：" << ltm->tm_mday << endl;
	cout << "时间：" << ltm->tm_hour << ":";
	cout << ltm->tm_min << ":";
	cout << ltm->tm_sec << endl;
}