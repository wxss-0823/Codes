#define   _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int max(int x, int y)
{
	return x > y ? x : y;
}

int main(void)
{
	/* p是函数指针 */
	int (*p)(int, int) = &max;
	int a, b, c, d;
	
	printf("please input three numbers:");
	scanf("%d %d %d", &a, &b, &c);

	/* 与直接调用函数等价 */
	d = p(p(a, b), c);

	printf("The max number is: %d\n", d);

	return 0;
}