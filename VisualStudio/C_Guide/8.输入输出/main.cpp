#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	char buff[255];
	/* 创建文件指着 */
	FILE* fp = NULL;

	/* 向文件写入内容 */
	fp = fopen("D:test.txt", "w+");
	fprintf(fp, "This is testing for fprintf...\n");
	fputs("This is testing for fputs...\n", fp);
	fclose(fp);
	
	/* 读取文件 */
	fp = fopen("D:test.txt", "r");
	fscanf(fp, "%s", buff);
	printf("1: %s\n", buff);

	fgets(buff, 255, fp);
	printf("2: %s\n", buff);

	fgets(buff, 255, fp);
	printf("3: %s\n", buff);
}