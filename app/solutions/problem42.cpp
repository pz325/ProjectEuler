/*
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
*/

#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>


// up to t_50
std::vector<unsigned> triangleNumber = {1, 3, 6, 10, 15, 21, 28, 
    36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 
    231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 
    561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 
    1035, 1081, 1128, 1176, 1225, 1275};

void generateTriangleNumber(unsigned n)
{
    for (unsigned i = 1; i <= n; i ++)
    {
        std::cout << i * (i + 1) / 2 << ", ";
    }
}

enum ParsingState { START_QUOTE, STRING, END_QUOTE, COMMA };
const int base = 64;

int main(int argc, char const *argv[])
{
    ParsingState state = START_QUOTE;

    // load problem42.txt
    std::ifstream fin;
    fin.open("problem42.txt", std::ios::in);
    unsigned char ch;
    int sum;
    int count = 0;
    while(!fin.eof()) {
        fin >> ch;
        // std::cout << ch << ": " ;
        switch(state){
            case START_QUOTE:
                // std::cout << "START_QUOTE" << std::endl;
                if (ch == '"') { 
                    sum = 0;
                    state = STRING;                    
                }
                break;
            case STRING:
                // std::cout << "STRING";
                if (ch != '"')
                {
                    // std::cout << "[" << static_cast<int>(ch) << "] " ;
                    sum += (static_cast<int>(ch) - base);
                }
                else {
                    state = END_QUOTE;
                    // std::cout << "sum: " << sum;
                    if (std::find(triangleNumber.begin(), triangleNumber.end(), sum) != triangleNumber.end())
                    {
                        ++count;
                    }
                }
                // std::cout << std::endl;
                break;
            case END_QUOTE:
                // std::cout << "END_QUOTE" << std::endl; 
                if (ch == ',') { 
                    state = COMMA;
                }
                break;
            case COMMA:
                // std::cout << "COMMA" << std::endl; 
                if (ch == '"') {
                    sum = 0;
                    state = STRING;
                }
                break;
        }
    }

    std::cout << "result: " << count << std::endl;
    return 0;base
}