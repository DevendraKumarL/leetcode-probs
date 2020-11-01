'''
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
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000 }
        num = 0
        i = 0
        while (i < len(s)):
            if (i == len(s) -1):
                num = num + roman[s[i]]
                i = i + 1
            elif ((s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'))
                  or (s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'))
                  or (s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'))):
                num = num + (roman[s[i+1]] - roman[s[i]])
                i = i + 2
            else:
                num = num + roman[s[i]]
                i = i + 1
        return num