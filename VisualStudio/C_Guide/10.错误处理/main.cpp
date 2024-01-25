#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

extern int errno;

int main()
{
	FILE* fp = NULL;
	int errnum;
	fp = fopen("unexist.txt", "rb");
	if (fp == NULL)
	{
		errnum = errno;
		fprintf(stderr, "错误号：%d\n", errnum);
		perror("通过 perror 输出错误");
		fprintf(stderr, "通过 strerror 输出错误：%s\n", strerror(errnum));
		exit(-1);
	}
	else
	{
		fclose(fp);
		exit(0);
	}
	return 0;
}