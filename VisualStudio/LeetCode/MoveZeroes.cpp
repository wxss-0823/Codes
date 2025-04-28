#include "Solution.h"

vector<int>& Solution::moveZeroes(vector<int>& nums) {
	 vector<int>::iterator ite = remove(nums.begin(), nums.end(), 0);
	 for (; ite != nums.end(); ite++) {
		 *ite = 0;
	 }
	 return nums;
}