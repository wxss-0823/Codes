#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

/* 定义结构体 */
struct Node
{
	char intro[20];
	struct Node* next_node;
};

int main()
{
	struct Node node1, node2;

	/* node1 详述 */
	strcpy(node1.intro, "This is node1.");
	node1.next_node = &node2;

	/* node2 详述 */
	strcpy(node2.intro, "This is node2.");
	node2.next_node = &node1;

	printf("%s\n", node1.next_node->intro);
	printf("%s\n", node2.next_node->intro);
	
	return 0;
}
