/*
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
*/

#include "util.h"
#include <iostream>
#include <cmath>

int main()
{
	long long N = 1000000;
	long long result = 0;
	for (long long i = 2; i < N; ++i)
	{
		std::vector<unsigned> digits = GetDigits(i);
		long long sum = 0;
		for (std::vector<unsigned>::iterator it = digits.begin(); it != digits.end(); ++it)
		{
			sum += pow(*it, 5);
		}
		if (sum == i)
		{
			std::cout << sum << std::endl;
			result += i;
		}
	}

	std::cout << "result: " << result << std::endl;
	return 0;
}