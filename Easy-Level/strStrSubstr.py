'''
    Problem:
    Implement strStr().
    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Example 1:
    Input: haystack = "hello", needle = "ll"
    Output: 2

    Example 2:
    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

    Example 3:
    Input: haystack = "", needle = ""
    Output: 0

    Solution(slow):
        -maintain a stack to push matching chars in given haystack needle
        -have needle pointer to track how many chars proccessed
        -loop index through the haystack until we reach end
            -if char matches in haystack needle push to stack
                if needle pointer reached end then break which is a match
            -else if stack not empty and needle was traversed
                -empty the stack
                -reset loop index = index - needle pointer + 1
                -reset needle pointer
            -else increment index
        -if needle pointer not end of needle return -1 which is not a match
        -return first element of stack
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 and len(needle) != 0:
            return -1
        if len(needle) == 0 or len(haystack) == 0:
            return 0
        stk = []
        j = 0
        i = 0
        while i < len(haystack):
            if needle[j] == haystack[i]:
                stk.append(i)
                j = j + 1
                i = i + 1
                if len(stk) == len(needle):
                    break
            elif len(stk) != 0 and j != 0:
                stk = []
                i = i - j + 1
                j = 0
            else:
                i = i + 1
        if len(stk) != len(needle):
            return -1
        return stk[0]
        