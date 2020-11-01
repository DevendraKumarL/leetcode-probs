'''
    Problem:
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    Example:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

    Solution:
    -Consider 1st string as the common prefix, store it's length in prefixLen
    -Traverse the array from 2nd string till the end
        -new prefix length i= min(currentStr, prefixLen)
        -until we find the common prefix in currentStr keep reducing prefixLen
        -while currentStr.startswith(prefixStr) == False -> prefixLen -=1
    -Return prefixStr[0:prefixLen]
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 0:
            prefixLen = len(strs[0])
            for s in strs[1:len(strs)]:
                prefixLen = min(len(s), prefixLen)
                while not s.startswith(strs[0][:prefixLen]):
                    prefixLen -= 1
            if prefixLen <= 0:
                return ""
            else:
                return strs[0][:prefixLen]
        return ""