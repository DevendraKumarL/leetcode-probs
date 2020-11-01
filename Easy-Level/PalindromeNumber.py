'''
    Problem:
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

    Example:
    Input: 121
    Output: true

    Solution1: (Slow)
    -Reverse the number and check it is same as the original number
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        sum = 0
        n = x
        dplace = len(str(n))
        while (n > 0):
            sum += (n % 10) * pow(10, dplace-1)
            dplace = dplace - 1
            n = int(n / 10)
        return sum == x