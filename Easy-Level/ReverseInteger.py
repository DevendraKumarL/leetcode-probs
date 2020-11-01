'''
    Problem:
    Given a 32-bit signed integer, reverse digits of an integer.

    Example:
    Input: 123
    Output: 321

    Solution: (Slow)
        -Convert to string, reverse and convert to int
'''

class Solution:
    def reverse(self, x: int) -> int:
        if (x < 0):
            s = str(-x)
            num = -int(s[::-1])
            if (abs(num) > (2 ** 31 -1)):
                return 0
            return num
        else:
            s = str(x)
            num = int(s[::-1])
            if (num > (2 ** 31 -1)):
                return 0
            return num