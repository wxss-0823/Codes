#include <stdio.h>

struct Book
{
	unsigned int a : 1;
	unsigned int b : 2;
	unsigned int c : 3;
};

int main()
{
	struct Book book1;
	book1.a = 1;
	book1.b = 3;
	book1.c = 7;
	printf("%d\n", book1.a);
	printf("%d\n", book1.b);
	printf("%d\n", book1.c);
}