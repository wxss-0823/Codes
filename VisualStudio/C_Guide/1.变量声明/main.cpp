#include <stdio.h>

// 函数定义变量 x 和 y
int x;
int y;
int addwonum()
{
	x = 1;
	y = 2;
	return x + y;
}

int main()
{
	int result;
	// 调用函数 addwonum
	result = addwonum();

	printf("result 为：%d", result);
	return 0;
}