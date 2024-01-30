#include <iostream>	

using namespace std;

class Box
{
public:
	Box()
	{
		cout << "Constructor Called." << endl;
	}
	~Box()
	{
		cout << "Deconstructor Called." << endl;
	}
};

int main()
{
	Box* boxarray = new Box[4];

	delete [] boxarray;
	return 0;
}