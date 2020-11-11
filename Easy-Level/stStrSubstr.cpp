/*
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
*/
class Solution {
public:
    int strStr(string haystack, string needle) {
        int i = 0, j = 0;
        while (true) { // loop through haystack
            j = 0; // loop through needle
            while (true) {
                if (j == needle.length()) return i; // j reached end of needle return i as the start index of match
                if (i + j == haystack.length()) return -1; // total length i + j reaches haystack size then return -1 no match found
                if (needle[j] != haystack[i+j]) break; // if needle j != haystack i to j then break to retry from current i of haystack
                j++;
            }
            i++;
        }
    }
};