/*
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
*/

#include "util.h"
#include <iostream>
#include <vector>


int main(int argc, char const *argv[])
{
	unsigned N = 1000000;
	unsigned sum = 0;
	for (unsigned i = 1; i < N; ++i)
	{
		std::vector<unsigned> digits_10 = GetDigits(i);
		std::vector<unsigned> digits_2 = GetBinary(i);
		if (IsPalindromic<unsigned>(digits_10) && IsPalindromic<unsigned>(digits_2))
		{
			std::cout << i << std::endl;
			std::for_each(digits_2.begin(), digits_2.end(), [](unsigned b) { std::cout << b; });
			std::cout << std::endl;
			sum += i;
		}
	}

	std::cout << "Result " << sum << std::endl;
	return 0;
}