/*
    Problem:
    Given a 32-bit signed integer, reverse digits of an integer.

    Example:
    Input: 123
    Output: 321

    Solution:
    -Get the length of the num by converting to string
    -Loop the below until num > 0
    -Perform n % 10 to get the last digit of the num
    -Accumulate sum += n % 10 * pow(10, len-1) // digit * 1000, 100, 10...
    -Reduce the num = num / 10 to remove out the last digit
*/

class Solution {
public:
    int reverse(int x) {
        int n = x < 0 ? (unsigned int)x*-1 : x;
        int len = to_string(n).length();
        int sum = 0;
        while (n > 0) {
            int dig = n % 10;
            long numToAdd = dig * pow(10, len-1);
            if (sum > INT_MAX - numToAdd) {
                return 0;
            }
            sum += numToAdd;
            len--;
            n = n / 10;
        }
        return x < 0 ? -sum : sum;
    }
};