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
		fprintf(stderr, "����ţ�%d\n", errnum);
		perror("ͨ�� perror �������");
		fprintf(stderr, "ͨ�� strerror �������%s\n", strerror(errnum));
		exit(-1);
	}
	else
	{
		fclose(fp);
		exit(0);
	}
	return 0;
}