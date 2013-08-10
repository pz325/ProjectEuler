/*
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
*/

#include "util.h"
#include <iostream>

int main()
{
	std::vector<std::pair<unsigned, unsigned>> ab;
	double tmp1, tmp2;
	for (unsigned a = 10; a <= 98; ++a)
	{
		for (unsigned b = a+1; b <= 99; ++b)
		{
			std::vector<unsigned> digits_a = GetDigits(a);
			std::sort(digits_a.begin(), digits_a.end());
			std::vector<unsigned> digits_b = GetDigits(b);
			std::sort(digits_b.begin(), digits_b.end());
			if (digits_a[0] == digits_b[0])
			{
				tmp1 = static_cast<double>(digits_a[1]) / static_cast<double>(digits_b[1]);
				tmp2 = static_cast<double>(a) / static_cast<double>(b);
				if (tmp1 == tmp2 && a % 10 != 0)
				{
					ab.push_back(std::make_pair(a, b));
				}
			}
			if (digits_a[1] == digits_b[1])
			{
				tmp1 = static_cast<double>(digits_a[0]) / static_cast<double>(digits_b[0]);
				tmp2 = static_cast<double>(a) / static_cast<double>(b);
				if (tmp1 == tmp2 && a % 10 != 0)
				{
					ab.push_back(std::make_pair(a, b));
				}
			}
		}
	}
	std::for_each(ab.begin(), ab.end(), 
		[](std::pair<unsigned, unsigned> p){ 
			std::cout << p.first << " " << p.second << std::endl;
		});

	return 0;
}