/*
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
*/

#include <iostream>

int main(int argc, char const *argv[])
{
    unsigned N = 1000;
    unsigned maxNumSolutions = 0;
    unsigned maxP = 0;
    unsigned a, b, c;
    for(unsigned p = 3; p <= N; ++p)
    {
        std::cout << p << std::endl;
        unsigned numSolution = 0;
        for(a = 1; a <= p; ++a)
        {
            for(b = a; b <= p; ++b)
            {
                c = p - a - b;
                if (a * a + b * b == c * c)
                {
                    std::cout << "{" << a << ", " << b << ", " << c << "}" << std::endl;
                    numSolution += 1;
                }
            }
        }
        if (numSolution > maxNumSolutions)
        {
            maxNumSolutions = numSolution;
            maxP = p;
        }
    }

    std::cout << "Result " << maxP << std::endl;
    return 0;
}