#include "Solution.h"
using namespace std;

int Solution::findVectorMaxElement(vector<int>& vec)
{
	int nLastValue = 0;
	auto it = vec.begin();
	while (it != vec.end())
	{
		nLastValue = *it > nLastValue ? *it : nLastValue;
		it++;
	}
	return nLastValue;
}


vector<bool> Solution::kidWithCandies(vector<int>& candies, int extraCandies)
{
	int nMaxElement = findVectorMaxElement(candies);
	auto iterator = candies.begin();
	vector<bool> bVectorResult;

	while (iterator != candies.end())
	{
		bVectorResult.push_back(*iterator + extraCandies >= nMaxElement ? true : false);
		iterator++;
	}

	return bVectorResult;
}