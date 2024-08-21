#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <stdlib.h>


struct Student {
	char name[10] = "wxss";
	int age = 22;
	int grades = 23;
	void (*print_info)();
}stu;

void print_info() 
{
	char buffer[3];
	char string[34];
	// 拼接字符串
	string[0] = '\0';
	strcat(string, stu.name);
	strcat(string, " is ");
	// 整形转字符串
	_itoa_s(stu.age, buffer, _countof(buffer), 10);

	strcat(string, buffer);

	strcat(string, " years old in grade ");

	_itoa_s(stu.grades, buffer, _countof(buffer), 10);

	strcat(string, buffer);

	strcat(string, ".");

	printf("%s", string);
}

struct Student stu1 = {"...", 0, 0, print_info};

int FuncPointerInit() {
	// 打印函数名地址
	// 函数名地址和函数名的值是同一个，即函数的首地址里面存放的是函数的首地址
	printf("The address of function is %p\n", print_info);
	printf("The address of print_info is %p\n", &print_info);
	stu1.print_info();
	printf(stu1.name);
	return 0;
}







