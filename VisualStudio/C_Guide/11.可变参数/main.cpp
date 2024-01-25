#include <stdio.h>
#include <stdarg.h>

double average(int num, ...)
{
	va_list valist;
	double sum = 0.0;
	int i;

	/* Ϊ num ��������ʼ��valist */
	va_start(valist, num);

	/* �������и��� valist �Ĳ��� */
	for (i = 0; i < num; i++)
	{
		// printf("%d\n", va_arg(valist, int));
		sum += va_arg(valist, int);
	}

	/* ����Ϊ valist �������ڴ� */
	va_end(valist);

	return sum / num;
}

int main()
{
	// average(3, 1, 2, 3);
	printf("Average of four numbers: %f\n", average(4, 23, 46, 26, 74));
	printf("Average of three numbers: %f", average(3, 3, 46, 2));

}