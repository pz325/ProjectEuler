/*
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
*/

#include "util.h"
#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    unsigned N = 1000000;
    unsigned numDigits;
    unsigned total = 0;
    unsigned index = 1;
    unsigned i = 1;
    std::vector<unsigned> d;
    std::vector<unsigned> digits;
    while(index <= N)
    {
        while(total < index)
        {
            digits = GetDigits(i);
            numDigits = digits.size();
            total += numDigits;
            ++i;
        }
        // std::cout << index << " " << total << " " << i-1 << " " << digits[numDigits - total + index - 1] << std::endl;
        d.push_back(digits[numDigits - total + index - 1]);
        index *= 10;
    }
    unsigned r = 1;
    std::for_each(d.begin(), d.end(), 
        [&r](unsigned x){
            std::cout << x << std::endl;
            r *= x;
        });
    std::cout << "result: " << r << std::endl;
    return 0;
}