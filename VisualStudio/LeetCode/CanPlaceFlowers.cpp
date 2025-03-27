#include "Solution.h"

bool Solution::canPlaceFlowers(vector<int>& flowerbed, int n)
{
	int nZeroCounter = 0;
	int nPositionCounter = 0;
	// find 3 consecutive 0
	for (int i = 0; i < flowerbed.size(); i++)
	{
		nZeroCounter = flowerbed[i] == 1 ? 0 : nZeroCounter + 1;
		if (nZeroCounter == flowerbed.size())
			nPositionCounter = nZeroCounter / 2 + nZeroCounter % 2;
		else if (i - nZeroCounter + 1 == 0)
			nPositionCounter = nZeroCounter / 2;
		else if(i == flowerbed.size() - 1)
			nPositionCounter += nZeroCounter / 2;
		else if (nZeroCounter >= 3 && flowerbed[i + 1] == 1)
			nPositionCounter += (nZeroCounter - 3) / 2 + 1;
	}

	// check nPositionCounter & n
	return nPositionCounter >= n ? true : false;
}