#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
/* # 运算符用于将任何变量转换为字符串 */
#define stringer( x ) printf( #x "\n")

int main()
{
	/* stringer的输入并不是字符串，宏定义会将其解释转换为字符串并输出 */
	stringer(134 sdaf +——=-);
}
