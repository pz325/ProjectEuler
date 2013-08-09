/*
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
*/

#include <iostream>     // std::cout
#include <algorithm>    // std::next_permutation, std::sort

int main () {
	int array[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

	std::sort (array, array+10);
	unsigned i = 1;
	unsigned N = 1000000;
	do 
	{
		++i;
	} while ( std::next_permutation(array, array+10) && i < N);
	for (unsigned i = 0; i < 10; ++i)
	{
		std::cout << array[i];
	}
	std::cout << std::endl;
	return 0;
}
