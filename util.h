#pragma once

#include <vector>
#include <algorithm>
#include <tuple>

std::vector<long long> GetPrimeFactors(long long x)
{
	std::vector<long long> primeFactors;
	if (x == 1)
	{
		return primeFactors;
	}
	while (x % 2 == 0)
	{
		primeFactors.push_back(2);
		x /= 2;
	}
	long long i = 3;
	while (i * i <= x)
	{
		while (x % i == 0)
		{
			x /= i;
			primeFactors.push_back(i);
		}
		i += 2;
	}
	if (x > 1)
	{
		primeFactors.push_back(x);
	}
    return primeFactors;
}

bool IsPrime(long long x)
{
	if (x == 1)
	{
		return false;
	}
	if (x == 2)
	{
		return true;
	}
	if (x % 2 == 0)
	{
		return false;
	}
	long long i = 3;
	while (i * i <= x)
	{
		if (x % i == 0)
		{
			return false;
		}
		i += 2;
	}
	if (x > 1)
	{
		return true;
	}
	return false;
}


std::vector<long long> GetPrimesLessThan(long long x)
{
	std::vector<long long> primes;
	for (long long i = 2; i < x; ++i)
	{
		if (IsPrime(i))
		{
			primes.push_back(i);
		}
	}
	return primes;
}

///
/// Can also be used for conversion of from decimal to the other number system
///
/// \param base
/// \return digits vector and number of digits tuple.
///
std::tuple<std::vector<unsigned>, unsigned> GetDigits(long long x, unsigned base=10)
{
	std::vector<unsigned> digits;
	unsigned num = 0;
	while(x > 0)
	{
		num += 1;
		digits.push_back(x % base);
		x /= base;
	}
	std::reverse(digits.begin(), digits.end());
	std::tuple<std::vector<unsigned>, unsigned> ret = std::make_tuple(digits, num);
	return ret;
}

template<class T>
bool IsPalindromic(std::vector<T> x)
{
	unsigned length = x.size();
	unsigned halfLength = x.size() / 2;
	for (unsigned i = 0; i < halfLength; ++i)
	{
		if (x[i] != x[length-i-1])
		{
			return false;
		}
	}
	return true;
}