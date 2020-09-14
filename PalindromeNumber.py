'''
    Problem:
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

    Example:
    Input: 121
    Output: true

    Solution1: (Slow)
    -Reverse the number and check it is same as the original nuber

    Solution2: (Fast)
    -x is original number
    -If x < 0 || (x % 10 != 0 && x != 0) then it is not a palindrome
    -Revert the last half of the number and check it is equal to the first half of the number
    -Revert last half of number: reverted = (reverted * 10) + x % 10. i.e., 10 + 2 = 12, 120 + 3 = 123
    -Condition that reaches the half the original number: x > reverted
    -Check reverted == x || reverted/10 == x - in case the number has odd length, we can ingnore the middle number
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