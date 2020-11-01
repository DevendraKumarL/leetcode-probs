/*
    Problem:
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

    There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900

    Example:
    Input: "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

    Solution: (Slow)
    -Store a map for the roman to int
    -Traverse the string, check if the char is is part of the subtraction, then consider i and i + 1
        -Get the number corresponding to the roman number at i in string s, sum the result
*/

class Solution {
public:
    int romanToInt(string s) {
        map<char, int> roman = {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C',100}, {'D', 500}, {'M', 1000}
        };
        int sum = 0, i = 0;
        while (i < s.length()) {
            if (i == s.length() - 1) {
                sum += roman[s.at(i)];
                i++;
            } else if ((s.at(i) == 'I' && (s.at(i+1) == 'V' || s.at(i+1) == 'X'))
                  || (s.at(i) == 'X' && (s.at(i+1) == 'L' || s.at(i+1) == 'C'))
                  || (s.at(i) == 'C' && (s.at(i+1) == 'D' || s.at(i+1) == 'M'))) {
                sum += (roman[s.at(i+1)] - roman[s.at(i)]);
                i += 2;
            } else {
                sum += roman[s.at(i)];
                i++;
            }
        }
        return sum;
    }
};