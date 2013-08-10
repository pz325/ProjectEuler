/*
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
*/

#include "util.h"
#include <iostream>
#include <tuple>

unsigned factorial[] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
int main()
{
	unsigned N = 2540161;
	std::vector<unsigned> factorialDigits;
	for(unsigned i = 10; i < N; ++i)
	{
		std::vector<unsigned> digits = std::get<0>(GetDigits(i));
		unsigned sum = 0;
		for(auto it = digits.begin(); it != digits.end(); ++it)
		{
			sum += factorial[*it];
		}
		if (sum == i)
		{
			factorialDigits.push_back(i);
		}
	}
	unsigned sum = 0;
	for(auto it = factorialDigits.begin(); it != factorialDigits.end(); ++it)
	{
		std::cout << *it << std::endl;
		sum += *it;
	}
    std::cout << "Result: " << sum << std::endl;
	return 0;
}