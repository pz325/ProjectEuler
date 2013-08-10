/*
Unit tests for util.h
*/

#include "util.h"
#include <vector>
#include <tuple>

#define BOOST_TEST_MODULE Util
#include <boost/test/unit_test.hpp>

BOOST_AUTO_TEST_SUITE(Util)

// GetDigits()
BOOST_AUTO_TEST_CASE(TestGetDigitsDecimal)
{
    unsigned x = 4012;
    auto ret = GetDigits(x);
    std::vector<unsigned> digits = std::get<0>(ret);
    unsigned num = std::get<1>(ret);
    BOOST_CHECK(digits[0] == 4);
    BOOST_CHECK(digits[1] == 0);
    BOOST_CHECK(digits[2] == 1);
    BOOST_CHECK(digits[3] == 2);
    BOOST_CHECK(num == 4);
}

// GetDigits() convert to binary
BOOST_AUTO_TEST_CASE(TestGetDigitsBinary)
{
    unsigned x = 18;   // 10010
    auto ret = GetDigits(x, 2);
    std::vector<unsigned> digits = std::get<0>(ret);
    unsigned num = std::get<1>(ret);
    BOOST_CHECK(digits[0] == 1);
    BOOST_CHECK(digits[1] == 0);
    BOOST_CHECK(digits[2] == 0);
    BOOST_CHECK(digits[3] == 1);
    BOOST_CHECK(digits[4] == 0);
    BOOST_CHECK(num == 5);
}

// GetPrimeFactors()
BOOST_AUTO_TEST_CASE(TestGetPrimeFactors)
{
    unsigned x = 20;  // {2 2 5}
    std::vector<long long> primeFactors = GetPrimeFactors(x);
    BOOST_CHECK(primeFactors[0] == 2);
    BOOST_CHECK(primeFactors[1] == 2);
    BOOST_CHECK(primeFactors[2] == 5);
}

// IsPrime()
BOOST_AUTO_TEST_CASE(TestIsPrime)
{
    BOOST_CHECK(IsPrime(1) == false);
    BOOST_CHECK(IsPrime(2) == true);
    BOOST_CHECK(IsPrime(13) == true);
}

// GetPrimesLessThan()
BOOST_AUTO_TEST_CASE(TestGetPrimesLessThan)
{
    unsigned x = 20;  // {2, 3, 5, 7, 11, 13, 17}
    std::vector<long long> primes = GetPrimesLessThan(x);
    BOOST_CHECK(primes[0] == 2);
    BOOST_CHECK(primes[1] == 3);
    BOOST_CHECK(primes[2] == 5);
    BOOST_CHECK(primes[3] == 7);
    BOOST_CHECK(primes[4] == 11);
    BOOST_CHECK(primes[5] == 13);
    BOOST_CHECK(primes[6] == 17);
}

// IsPalindromic()
BOOST_AUTO_TEST_CASE(TestIsPalindromic)
{
    BOOST_CHECK(IsPalindromic<unsigned>(std::get<0>(GetDigits(12321))) == true);
    BOOST_CHECK(IsPalindromic<unsigned>(std::get<0>(GetDigits(1))) == true);
    BOOST_CHECK(IsPalindromic<unsigned>(std::get<0>(GetDigits(11))) == true);
    BOOST_CHECK(IsPalindromic<unsigned>(std::get<0>(GetDigits(1234))) == false);
    BOOST_CHECK(IsPalindromic<unsigned>(std::get<0>(GetDigits(12234))) == false);
}


BOOST_AUTO_TEST_SUITE_END()