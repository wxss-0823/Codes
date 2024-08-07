#define CTGR_NUM 4 
#define STU_NUM 10

enum Grade {
	D,
	C,
	B,
	A
};

struct Assessment {
	enum Grade Eng_G;
	int Grade_std[CTGR_NUM];
	float Grades[STU_NUM];
	char Eng_Grades[STU_NUM];
};

void Check_CATA();

void TestInit();
