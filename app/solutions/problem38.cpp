/*
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
*/

#include "util.h"
#include <vector>
#include <set>
#include <iostream>

int main(int argc, char const *argv[])
{
	unsigned N = 98765;
	unsigned max = 0;
	for(unsigned i = 1; i <= N; ++i)
	{
		std::set<unsigned> pandigital;
		std::vector<unsigned> result;
		unsigned num = 0;
		unsigned tmp;
		unsigned j = 1;
		while(true)
		{	
			tmp = i * j;
			std::vector<unsigned> digits = GetDigits(tmp);
			result.insert(result.end(), digits.begin(), digits.end());
			// ignore 0
			if (std::find(digits.begin(), digits.end(), 0) != digits.end())
			{
				break;
			}
			for(auto it = digits.begin(); it != digits.end(); ++it)
			{
				pandigital.insert(*it);
			}
			// check number of concatenated digits
			num += digits.size();
			if (num > 9)
			{
				break;
			}
			if (num == 9)
			{
				if (pandigital.size() == 9)
				{
					std::for_each(result.begin(), result.end(), [](unsigned d){ std::cout << d; });
					std::cout << std::endl;
				}
			}
			++j;
		}
	}
	return 0;
}