#include <stdio.h>;

void Pointer_test() {
	char a[20] = "You_are_a_good_girl";
	char* p = a;
	char** ptr = &p;
	printf(p);
}
