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
		printf("%d�Ľ׳��ǣ�%d\t\t", i, factorial(i));
		printf("��%d��쳲����������ǣ�%d\n", i, fibonaci(i));
	}
	return 0;
}