#include <stdio.h>

// ����������� x �� y
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
	// ���ú��� addwonum
	result = addwonum();

	printf("result Ϊ��%d", result);
	return 0;
}