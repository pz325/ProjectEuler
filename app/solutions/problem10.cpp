/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

#include "util.h"
#include <iostream>


int main()
{
	long long N = 2000000;
	long long sum = 0;
	for (long long i = 2; i < N; ++i)
	{
		if (IsPrime(i))
		{
			sum += i;
		}
	}
	std::cout << "result: " << sum << std::endl;
}