#include <stdio.h>
#include <stdlib.h>

int factorial(unsigned int i)
{
	if (i == 1)
	{
		return 1;
	}
	else if (i == 0)
	{
		return 1;
	}
	return i * factorial(i - 1);
}

int fibonaci(int i)
{
	if (i == 0)
	{
		return 0;
	}
	if (i == 1)
	{
		return 1;
	}
	return fibonaci(i - 1) + fibonaci(i - 2);
}

int main()
{
	int i;
	for (i = 0; i < 10; i++)
	{
		printf("%d的阶乘是：%d\t\t", i, factorial(i));
		printf("第%d个斐波那契数列是：%d\n", i, fibonaci(i));
	}
	return 0;
}