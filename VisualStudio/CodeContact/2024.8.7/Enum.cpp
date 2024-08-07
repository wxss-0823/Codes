#include <stdio.h>

#define CTGR_NUM 4 
#define STU_NUM 10

// �ɼ��ȼ�����
enum Grade{
	D,
	C,
	B,
	A
};

// �ṹ�壺����
/*
	vs ��֧���ڽṹ�����ָ�����
*/

struct Assessment {
	int Grade_std[CTGR_NUM] = { 60, 70, 80, 90 };
	float Grades[STU_NUM] = { 41.1, 62.2, 53.3, 84.4, 55.5, 76.6, 97.7, 98.8, 59.9, 60.0 };;
	char Eng_Grades[STU_NUM];
}assess;

// ���������ɼ��������
void Check_CATA() {
	for (int i = 0; i < STU_NUM; i++)
	{
		if (assess.Grades[i] <= assess.Grade_std[D]) {
			// ָ�벻�ܷ��ʳ�Ա����
			assess.Eng_Grades[i] = 'D';
		}
		else if (assess.Grades[i] <= assess.Grade_std[C]) {
			assess.Eng_Grades[i] = 'C';
		}
		else if (assess.Grades[i] <= assess.Grade_std[B]) {
			assess.Eng_Grades[i] = 'B';
		}
		else {
			assess.Eng_Grades[i] = 'A';
		}
	}
}

struct Assessment* assess1 = &assess;

// ���������ɼ��������
void Check_CATA1() {
	for (int i = 0; i < STU_NUM; i++)
	{
		if ((*assess1).Grades[i] <= (*assess1).Grade_std[D]) {
			// ָ�벻�ܷ��ʳ�Ա����
			// (*p).xxx[1] = xxx;
			// p->str ��ʾ p ���ڴ�� str �ĵ�ַ
			(*assess1).Eng_Grades[i] = 'D';
		}
		else if ((*assess1).Grades[i] <= (*assess1).Grade_std[C]) {
			(*assess1).Eng_Grades[i] = 'C';
		}
		else if ((*assess1).Grades[i] <= (*assess1).Grade_std[B]) {
			(*assess1).Eng_Grades[i] = 'B';
		}
		else {
			(*assess1).Eng_Grades[i] = 'A';
		}
	}
}

void TestInit() {
	Check_CATA1();
	printf((*assess1).Eng_Grades);
}